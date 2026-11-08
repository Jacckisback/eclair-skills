#!/usr/bin/env python3
"""Validate the example's file digests and key native-v2 constraints offline.
This deliberately does NOT replace `php tools/validate.php` from Éclair CMS.
"""
from pathlib import Path
import json,hashlib,re,sys
root=Path(__file__).resolve().parents[1]
source=root/'examples/extensions/skill-sample'
m=json.loads((source/'extension.json').read_text(encoding='utf-8'))
issues=[]
if m.get('schema')!='eclair-extension/1':issues.append('Wrong schema')
if not re.fullmatch(r'[a-z][a-z0-9-]{1,39}',m.get('id','')):issues.append('Invalid id')
if m.get('id')!=source.name:issues.append('Folder/id mismatch')
if any(r.get('method','GET')!='GET' for r in m.get('routes',{}).get('public',[])):issues.append('Public routes must be GET')
for f,sha in m.get('files',{}).items():
    p=source/f
    if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=sha:issues.append(f'Digest mismatch: {f}')
for p in source.rglob('*'):
    if p.is_file() and p.name!='extension.json' and p.relative_to(source).as_posix() not in m.get('files',{}):issues.append(f'Undeclared file: {p}')
for issue in issues:print('ERROR:',issue)
if issues:sys.exit(1)
print('PASS: offline example manifest and SHA-256 checks (not official core validation)')
