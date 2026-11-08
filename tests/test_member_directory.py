"""Offline packaging/integrity tests, separate from native Eclair HTTP tests."""
from pathlib import Path
import json,subprocess,sys,tempfile,unittest,shutil
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from verify_member_directory import validate
class MemberDirectoryTests(unittest.TestCase):
    def test_extension_integrity(self):
        self.assertEqual(validate(),[])
    def test_php_scenario(self):
        proc=subprocess.run(['php',str(ROOT/'tests/member-directory.php')],capture_output=True,text=True)
        self.assertEqual(proc.returncode,0,proc.stdout+proc.stderr)
        self.assertIn('isolated PHP assertions',proc.stdout)
    def test_tampering_refused(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'member-directory'
            shutil.copytree(ROOT/'examples/extensions/member-directory',p)
            with (p/'extension.php').open('a') as f:f.write('\n//tampered\n')
            self.assertTrue(any('SHA differs' in s for s in validate(p)))
    def test_unlisted_file_refused(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'member-directory';shutil.copytree(ROOT/'examples/extensions/member-directory',p)
            (p/'extra.php').write_text('<?php echo 1;')
            self.assertTrue(any('Listed files mismatch' in s for s in validate(p)))
    def test_public_post_contract_strict(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'member-directory';shutil.copytree(ROOT/'examples/extensions/member-directory',p)
            m=json.loads((p/'extension.json').read_text())
            m['routes']['public'].append({'path':'/register','method':'POST','handler':'register','cache':False})
            (p/'extension.json').write_text(json.dumps(m))
            self.assertTrue(any('Experimental public routes mismatch' in s for s in validate(p)))
    def test_public_post_never_cached(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'member-directory';shutil.copytree(ROOT/'examples/extensions/member-directory',p)
            m=json.loads((p/'extension.json').read_text());m['routes']['public'][1]['cache']=True
            (p/'extension.json').write_text(json.dumps(m))
            self.assertTrue(any('cache=false' in s for s in validate(p)))
    def test_email_flows_scenario(self):
        proc=subprocess.run(['php',str(ROOT/'tests/member-enroll.php')],capture_output=True,text=True)
        self.assertEqual(proc.returncode,0,proc.stdout+proc.stderr)
        self.assertIn('isolated member enrollment/recovery assertions',proc.stdout)
    def test_public_scenario(self):
        proc=subprocess.run(['php',str(ROOT/'tests/member-public.php')],capture_output=True,text=True)
        self.assertEqual(proc.returncode,0,proc.stdout+proc.stderr)
        self.assertIn('isolated public-auth assertions',proc.stdout)
if __name__=='__main__': unittest.main()
