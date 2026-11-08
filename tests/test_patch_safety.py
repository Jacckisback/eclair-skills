"""Test the guarded patcher against synthetic fixtures; never touches real GitHub or a production checkout."""
from pathlib import Path
import ast, subprocess, sys, tempfile, unittest
ROOT=Path(__file__).resolve().parents[1]
SCRIPT=ROOT/'core-patch/apply_public_post.py'
TREE=ast.parse(SCRIPT.read_text())
def literal(name):
    for node in TREE.body:
        if isinstance(node,ast.Assign) and any(isinstance(x,ast.Name) and x.id==name for x in node.targets):
            return ast.literal_eval(node.value)
    raise KeyError(name)
def run(*args,cwd=None):
    return subprocess.run(list(args),cwd=cwd,capture_output=True,text=True)
class PatchSafety(unittest.TestCase):
    def setup_repo(self,root,version='2.0.0'):
        (root/'eclair/app/lib').mkdir(parents=True)
        (root/'docs/schemas').mkdir(parents=True)
        (root/'eclair/index.php').write_text(f"<?php define('ECLAIR_VERSION', '{version}');")
        needle=literal('needle'); anchor=literal('a')
        src=("<?php\nnamespace Eclair;\nclass Extensions {\n"
             +"    public static function validateDemo($m) {\n"
             +anchor+" || false) { }\n        }\n    }\n"
             +needle+"}\n")
        (root/'eclair/app/lib/Extensions.php').write_text(src)
        (root/'docs/schemas/extension.schema.json').write_text('{"properties":{"method": { "enum": ["GET"] }}}')
        run('git','init','-q','-b','main',str(root))
        run('git','config','user.email','tester@example.org',cwd=root)
        run('git','config','user.name','Tester',cwd=root)
        run('git','add','.',cwd=root)
        self.assertEqual(run('git','commit','-qm','fixture',cwd=root).returncode,0)
    def call(self,root,apply=False):
        cmd=[sys.executable,str(SCRIPT),'--checkout',str(root)]
        if apply:cmd+=['--apply']
        return run(*cmd)
    def test_dry_run_only(self):
        with tempfile.TemporaryDirectory() as d:
            r=Path(d);self.setup_repo(r)
            before=(r/'eclair/app/lib/Extensions.php').read_text()
            p=self.call(r)
            self.assertEqual(p.returncode,0,p.stdout+p.stderr)
            self.assertEqual(before,(r/'eclair/app/lib/Extensions.php').read_text())
    def test_reject_main(self):
        with tempfile.TemporaryDirectory() as d:
            r=Path(d);self.setup_repo(r)
            p=self.call(r,True)
            self.assertNotEqual(p.returncode,0)
            self.assertIn('main/master',p.stderr+p.stdout)
    def test_feature_branch_patch(self):
        with tempfile.TemporaryDirectory() as d:
            r=Path(d);self.setup_repo(r)
            self.assertEqual(run('git','checkout','-qb','feat/login',cwd=r).returncode,0)
            p=self.call(r,True)
            self.assertEqual(p.returncode,0,p.stdout+p.stderr)
            s=(r/'eclair/app/lib/Extensions.php').read_text()
            self.assertIn('Security::checkFormToken()',s)
            self.assertIn("['GET', 'POST']",s)
            self.assertIn("Cache-Control: private, no-store",s)
            self.assertIn("Http::redirect(path_to($to), 303)",s)
            self.assertIn('[200, 400, 401, 403, 409, 422, 429, 500, 503]',s)
            self.assertIn('ECLAIR_MEMBER_TRUSTED_PROXY_IP',s)
            self.assertIn('inet_pton($trustedProxy) === inet_pton($remoteIp)',s)
            lint=run('php','-l',str(r/'eclair/app/lib/Extensions.php'))
            self.assertEqual(lint.returncode,0,lint.stdout+lint.stderr)
            p2=self.call(r,True)
            self.assertNotEqual(p2.returncode,0,'second patch refused because worktree dirty')
    def test_reject_wrong_version(self):
        with tempfile.TemporaryDirectory() as d:
            r=Path(d);self.setup_repo(r,'2.0.1')
            self.assertEqual(run('git','checkout','-qb','feat/login',cwd=r).returncode,0)
            p=self.call(r,True)
            self.assertNotEqual(p.returncode,0)
            self.assertIn('expected Éclair 2.0.0',p.stderr+p.stdout)
    def test_reject_changed_source(self):
        with tempfile.TemporaryDirectory() as d:
            r=Path(d);self.setup_repo(r)
            self.assertEqual(run('git','checkout','-qb','feat/login',cwd=r).returncode,0)
            file=r/'eclair/app/lib/Extensions.php'
            file.write_text(file.read_text().replace('Route publique', 'Route personnalisée'))
            # Commit changed fixture to demonstrate branch clean but unexpected source.
            run('git','add','.',cwd=r);run('git','commit','-qm','other change',cwd=r)
            p=self.call(r,True)
            self.assertNotEqual(p.returncode,0)
            self.assertIn('anchor changed',p.stderr+p.stdout)
    def test_refuse_dirty_worktree(self):
        with tempfile.TemporaryDirectory() as d:
            r=Path(d);self.setup_repo(r)
            run('git','checkout','-qb','feat/login',cwd=r)
            (r/'extra.txt').write_text('pending')
            p=self.call(r,True)
            self.assertNotEqual(p.returncode,0)
            self.assertIn('dirty',p.stderr+p.stdout)
if __name__=='__main__':unittest.main()
