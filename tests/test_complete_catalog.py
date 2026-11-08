import hashlib,json,shutil,sys,tempfile,unittest,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from install_skills import choose,install
from validate_skills import validate

class CatalogTests(unittest.TestCase):
    def test_all_57_skills(self):
        self.assertEqual(validate(ROOT),[])
        cat=json.loads((ROOT/'catalog.json').read_text())
        self.assertEqual(len(cat['skills']),57)
        self.assertEqual({k:v['count'] for k,v in cat['groups'].items()},
            {'foundation':8,'commerce':10,'lms':7,'community':6,'business':8,'design':7,'seo':5,'integrations':6})
    def test_family_install_subset(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);install(ROOT,root,categories=['commerce'])
            names={p.name for p in (root/'.agents/skills').iterdir()}
            self.assertEqual(len(names),10)
            self.assertIn('eclair-commerce-pro',names)
            install(ROOT,root,categories=['seo'])
            self.assertEqual(len(list((root/'.agents/skills').iterdir())),15)
            with self.assertRaises(FileExistsError):install(ROOT,root,categories=['commerce'])
    def test_collision_is_atomic(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);install(ROOT,root,names=['eclair-seo-audit'])
            with self.assertRaises(FileExistsError):install(ROOT,root,categories=['seo'])
            self.assertEqual(len(list((root/'.agents/skills').iterdir())),1)
    def test_unknown_family_rejected(self):
        with self.assertRaises(ValueError):choose(ROOT,categories=['nothing'])
    def test_demo_manifest_integrity(self):
        d=ROOT/'examples/extensions/catalogue-demo'
        m=json.loads((d/'extension.json').read_text())
        self.assertEqual(m['schema'],'eclair-extension/1')
        self.assertEqual(m['routes']['public'],[{'method':'GET','path':'/catalogue-demo','handler':'page','cache':True}])
        self.assertEqual(set(p.name for p in d.iterdir()),{'extension.json','extension.php'})
        self.assertEqual(hashlib.sha256((d/'extension.php').read_bytes()).hexdigest(),m['files']['extension.php'])
        proc=subprocess.run(['php','-l',str(d/'extension.php')],capture_output=True,text=True)
        self.assertEqual(proc.returncode,0,proc.stderr)
    def test_no_unfinished_skill_pages(self):
        for entry in json.loads((ROOT/'catalog.json').read_text())['skills']:
            s=(ROOT/'skills'/entry['name']/'SKILL.md').read_text()
            self.assertNotIn('TODO: implement',s)
            self.assertIn('name: '+entry['name'],s)

if __name__=='__main__':unittest.main()
