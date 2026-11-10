import hashlib,json,shutil,sys,tempfile,unittest,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from install_skills import choose,install
from validate_skills import validate

class CatalogTests(unittest.TestCase):
    def test_all_skills(self):
        self.assertEqual(validate(ROOT),[])
        cat=json.loads((ROOT/'catalog.json').read_text())
        self.assertEqual(len(cat['skills']),200)
        self.assertEqual(len(cat['groups']),18)
        self.assertEqual(sum(v['count'] for v in cat['groups'].values()),200)
        self.assertEqual(len({s['name'] for s in cat['skills']}),200)
    def test_family_install_subset(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);install(ROOT,root,categories=['commerce'])
            names={p.name for p in (root/'.agents/skills').iterdir()}
            self.assertEqual(len(names),22)
            self.assertIn('eclair-commerce-pro',names)
            install(ROOT,root,categories=['seo'])
            self.assertEqual(len(list((root/'.agents/skills').iterdir())),33)
            with self.assertRaises(FileExistsError):install(ROOT,root,categories=['commerce'])
    def test_translated_install(self):
        langs=json.loads((ROOT/'catalog.json').read_text())['languages']['translations']
        self.assertEqual(langs,['en','es','de','it','pt'])
        for lang in langs:
            with tempfile.TemporaryDirectory() as d:
                root=Path(d);install(ROOT,root,names=['eclair-contact-forms','eclair-architecture'],lang=lang)
                fr=(ROOT/'skills/eclair-contact-forms/SKILL.md').read_text()
                tr=(root/'.agents/skills/eclair-contact-forms/SKILL.md').read_text()
                self.assertNotEqual(fr,tr)
                self.assertIn('name: eclair-contact-forms',tr)
                self.assertTrue((root/'.agents/skills/eclair-architecture/references/core-map.md').is_file())
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(ValueError):install(ROOT,Path(d),names=['eclair-forum'],lang='xx')
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
