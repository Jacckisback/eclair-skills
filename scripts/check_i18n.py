#!/usr/bin/env python3
"""Check translation data in i18n/<lang>/ against the French source (stdlib only).

Verifies, for every translated language: same skills and fields, no empty value, no value
left identical to French (except names), same {placeholders} and same `backtick` spans in
templates, same headings in foundation files, front matter untouched.
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_skills as b  # noqa: E402

ROOT = b.ROOT
PH = re.compile(r'\{\w+\}')
TICK = re.compile(r'`[^`\n]+`')


def walk(src, dst, path, errors):
    if isinstance(src, dict):
        if not isinstance(dst, dict) or set(src) != set(dst):
            errors.append(f'{path}: keys differ')
            return
        for k in src:
            walk(src[k], dst[k], f'{path}.{k}', errors)
    else:
        if not isinstance(dst, str) or not dst.strip():
            errors.append(f'{path}: empty')
            return
        if sorted(PH.findall(src)) != sorted(PH.findall(dst)):
            errors.append(f'{path}: placeholders differ')
        if sorted(TICK.findall(src)) != sorted(TICK.findall(dst)):
            errors.append(f'{path}: backtick spans differ')
        if src.count('\n') != dst.count('\n'):
            errors.append(f'{path}: line count differs')


def check(lang):
    errors = []
    d = ROOT / 'i18n' / lang
    fr_tpl = json.loads((ROOT / 'i18n/fr/templates.json').read_text(encoding='utf-8'))
    try:
        tpl = json.loads((d / 'templates.json').read_text(encoding='utf-8'))
        walk(fr_tpl, tpl, 'templates', errors)
    except (OSError, ValueError) as exc:
        errors.append(f'templates.json: {exc}')
    fields = {}
    for f in sorted(d.glob('skills_*.json')):
        try:
            fields.update(json.loads(f.read_text(encoding='utf-8')))
        except ValueError as exc:
            errors.append(f'{f.name}: {exc}')
    source = {s['name']: s for _f, s, _l in b.all_templated()}
    for name in sorted(set(source) - set(fields)):
        errors.append(f'{name}: not translated')
    for name in sorted(set(fields) - set(source)):
        errors.append(f'{name}: unknown skill')
    same = 0
    for name, text in fields.items():
        if name not in source:
            continue
        if set(text) != set(b.TEXT_FIELDS):
            errors.append(f'{name}: fields differ')
            continue
        for k in b.TEXT_FIELDS:
            v = text[k]
            if not isinstance(v, str) or not v.strip():
                errors.append(f'{name}.{k}: empty')
            elif v.rstrip().endswith('.') and k != 'wp':
                errors.append(f'{name}.{k}: trailing period')
            elif '"' in v and k == 'goal':
                errors.append(f'{name}.{k}: double quote in goal')
            elif k not in ('wp', 'title', 'model') and v == source[name][k]:
                same += 1
                errors.append(f'{name}.{k}: identical to French')
    fmap = json.loads((ROOT / 'i18n/foundation-map.json').read_text(encoding='utf-8'))
    inv = {}
    for path, key in fmap.items():
        inv.setdefault(key, path)
    for key, path in sorted(inv.items()):
        src = (ROOT / 'skills' / path).read_text(encoding='utf-8')
        f = d / 'foundation' / key
        if not f.is_file():
            errors.append(f'foundation/{key}: missing')
            continue
        dst = f.read_text(encoding='utf-8')
        if len(re.findall(r'^#+ ', src, re.M)) != len(re.findall(r'^#+ ', dst, re.M)):
            errors.append(f'foundation/{key}: heading count differs')
        if src.startswith('---\n'):
            fm = src[:src.index('\n---\n', 4) + 5]
            if not dst.startswith(fm):
                errors.append(f'foundation/{key}: front matter changed')
        if sorted(TICK.findall(src)) != sorted(TICK.findall(dst)):
            errors.append(f'foundation/{key}: backtick spans differ')
        if dst.strip() == src.strip():
            errors.append(f'foundation/{key}: not translated')
    return errors, len(fields)


def main():
    langs = sys.argv[1:] or list(b.TRANSLATED)
    failed = False
    for lang in langs:
        errors, n = check(lang)
        if errors:
            failed = True
            print(f'FAIL [{lang}] {len(errors)} problem(s):\n- ' + '\n- '.join(errors[:25]))
        else:
            print(f'PASS [{lang}] {n} skills, templates and foundation files consistent with French')
    return 1 if failed else 0


if __name__ == '__main__':
    sys.exit(main())
