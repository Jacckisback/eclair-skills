#!/usr/bin/env python3
"""Offline integrity/shape check for a native Éclair 2.0 example extension.
This is NOT the authoritative core validator or a production security audit.
"""
from pathlib import Path
import hashlib,json,re,subprocess,sys

ROOT=Path(__file__).resolve().parents[1]
EXT=ROOT/'examples/extensions/member-directory'

def validate(path=EXT):
    errors=[]
    try:
        m=json.loads((path/'extension.json').read_text(encoding='utf-8'))
    except (ValueError,OSError) as exc:
        return [f'Unreadable manifest: {exc}']
    if m.get('schema')!='eclair-extension/1':errors.append('Not native eclair-extension/1')
    if m.get('id')!=path.name or not re.fullmatch(r'[a-z][a-z0-9-]{1,39}',m.get('id','')):
        errors.append('Invalid ID/folder')
    if m.get('requires',{}).get('eclair')!='>=2.0.0':errors.append('Target must be Éclair 2.0')
    public=m.get('routes',{}).get('public',[])
    expected_public={('GET','/membres/connexion','loginPage'),('POST','/membres/connexion','login'),
                     ('GET','/membres/espace','profilePage'),('POST','/membres/deconnexion','logout')}
    for route_path,handler in [('/membres/inscription','signup'),('/membres/verification','verify'),
                         ('/membres/recuperation','recover'),('/membres/reinitialisation','reset')]:
        expected_public.add(('GET',route_path,handler+'Page'))
        expected_public.add(('POST',route_path,handler))
    if {(r.get('method'),r.get('path'),r.get('handler')) for r in public}!=expected_public:
        errors.append('Experimental public routes mismatch')
    if any(r.get('cache') is not False for r in public):
        errors.append('Public member routes must all have cache=false')
    admins=m.get('routes',{}).get('admin',[])
    expected={('GET','','adminPage'),('POST','/create','create'),('POST','/disable','disable')}
    if {(r.get('method'),r.get('path'),r.get('handler')) for r in admins}!=expected:
        errors.append('Admin route mismatch')
    if any(r.get('right')!='users' for r in admins):errors.append('Admin routes need users permission')
    files=m.get('files',{})
    if not isinstance(files,dict) or not files:errors.append('Missing hashes')
    else:
        actual={f.relative_to(path).as_posix() for f in path.rglob('*') if f.is_file() and f.name!='extension.json'}
        if actual!=set(files): errors.append(f'Listed files mismatch: {sorted(actual^set(files))}')
        for rel,sha in files.items():
            if not re.fullmatch(r'[a-f0-9]{64}',sha):errors.append(f'Invalid SHA for {rel}');continue
            dest=(path/rel).resolve()
            if not dest.is_relative_to(path.resolve()) or not dest.is_file() or dest.is_symlink():
                errors.append(f'Illegal path: {rel}');continue
            if hashlib.sha256(dest.read_bytes()).hexdigest()!=sha:errors.append(f'SHA differs: {rel}')
            if rel.endswith('.php'):
                proc=subprocess.run(['php','-l',str(dest)],capture_output=True,text=True)
                if proc.returncode!=0:errors.append(f'PHP syntax fail: {rel}: {proc.stderr}')
    return errors

if __name__=='__main__':
    errors=validate()
    if errors:
        print('\n'.join('FAIL: '+e for e in errors));sys.exit(1)
    print('PASS: member-directory v0.3 experimental manifest/paths/digests/PHP syntax — offline only')
