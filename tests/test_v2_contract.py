import json, subprocess,sys,tempfile,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from check_core import check_core
from validate_skills import validate
from install_skills import install
class NativeV2ContractTests(unittest.TestCase):
    def test_complete_skills(self):self.assertEqual(validate(ROOT),[])
    def test_native_sample(self):
        p=subprocess.run([sys.executable,str(ROOT/'scripts/verify_sample.py')],capture_output=True,text=True)
        self.assertEqual(p.returncode,0,p.stdout+p.stderr)
    def test_php_syntax(self):
        p=subprocess.run(['php','-l',str(ROOT/'examples/extensions/skill-sample/extension.php')],capture_output=True,text=True)
        self.assertEqual(p.returncode,0,p.stdout+p.stderr)
    def test_guard_legacy_version(self):
        with tempfile.TemporaryDirectory() as d:
            r=Path(d);(r/'eclair').mkdir();(r/'eclair/index.php').write_text("<?php define('ECLAIR_VERSION', '1.14.2');")
            self.assertTrue(any('2.x' in x for x in check_core(r)))
    def test_installer_no_overwrite(self):
        with tempfile.TemporaryDirectory() as d:
            r=Path(d);install(ROOT,r)
            self.assertEqual(len(list((r/'.agents/skills').iterdir())),200)
            with self.assertRaises(FileExistsError):install(ROOT,r)
    def test_manifest_has_files_and_v2(self):
        m=json.loads((ROOT/'examples/extensions/skill-sample/extension.json').read_text())
        self.assertEqual(m['requires']['eclair'],'>=2.0.0')
        self.assertEqual(m['schema'],'eclair-extension/1')
        self.assertEqual(len(m['files']),1)
if __name__=='__main__':unittest.main()
