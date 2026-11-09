#!/usr/bin/env python3
"""Generate the six README files and their localized SVG diagrams.

    python3 scripts/build_readmes.py          # write README*.md + docs/assets/<lang>/*.svg
    python3 scripts/build_readmes.py --check  # fail if generated files are out of date

Texts live in scripts/readme_data_text.py and scripts/readme_data_skills.py.
Skill list, families and maturity come from catalog.json (single source of truth).
Standard library only.
"""
import argparse
import json
import re
import sys
from pathlib import Path
from xml.sax.saxutils import escape

sys.path.insert(0, str(Path(__file__).resolve().parent))
from readme_data_skills import LANGS, SKILLS  # noqa: E402
from readme_data_text import T  # noqa: E402
from readme_data_families import FAMILIES, CORE_STATUS, WORDPRESS, LAYER_LABELS  # noqa: E402
import build_skills  # noqa: E402

# Merge the generated skills (French line derived from the goal) and the new families.
_SPECS = build_skills.specs()
for _rows in _SPECS.values():
    for _s in _rows:
        _fr = _s['goal'][0].upper() + _s['goal'][1:] + '.'
        SKILLS[_s['name']] = (_s['en'], _fr, _s['es'], _s['de'], _s['it'], _s['pt'])
WP_EQUIV = {_s['name']: _s['wp'] for _rows in _SPECS.values() for _s in _rows}
for _i, _lang in enumerate(LANGS):
    for _key, _names in FAMILIES.items():
        T[_lang]['fam'][_key] = _names[_i]
    T[_lang]['mat']['core'] = CORE_STATUS[_i][0]
    T[_lang]['legend'] = T[_lang]['legend'].replace(' — ', ' — ' + CORE_STATUS[_i][1], 1)

ROOT = Path(__file__).resolve().parents[1]
REPO = 'https://github.com/Jacckisback/eclair-skills'
ORDER = build_skills.ORDER
COLORS = dict(foundation='#475569', commerce='#EA580C', lms='#2563EB', community='#7C3AED',
              business='#0D9488', design='#DB2777', seo='#16A34A', integrations='#0891B2',
              content='#4F46E5', media='#C026D3', components='#9333EA', multilingual='#0284C7', forms='#D97706',
              marketing='#E11D48', performance='#65A30D', security='#B91C1C', admin='#334155', developer='#0F766E')
EMOJI = dict(foundation='🧱', commerce='🛒', lms='🎓', community='💬', business='🗂️', design='🎨', seo='🔎', integrations='🔌',
             content='📝', media='🖼️', components='🧩', multilingual='🌍', forms='📮', marketing='📣',
             performance='⚡', security='🛡️', admin='🛠️', developer='💻')
LAYERS = [['commerce', 'lms', 'community', 'business', 'forms', 'marketing', 'integrations'],
          ['content', 'media', 'components', 'design', 'multilingual'],
          ['seo', 'performance', 'security'],
          ['foundation', 'admin', 'developer']]
MATURITY = {'workflow-native-v2': 'native', 'native-v2-workflow': 'native',
            'public-read-only-prototype-possible': 'readonly',
            'design-workflow-requires-verified-core-capabilities': 'design',
            'partly-blocked-by-core-contract': 'partial',
            'core-builtin-configuration-workflow': 'core'}
COL_FAM = dict(en=('Family', 'Scope'), fr=('Famille', 'Portée'), es=('Familia', 'Alcance'), de=('Familie', 'Umfang'), it=('Famiglia', 'Ambito'), pt=('Família', 'Âmbito'))
MAT_ORDER = ['core', 'native', 'readonly', 'partial', 'design']
MAT_ICON = dict(core='🟣', native='🟢', readonly='🔵', design='🟠', partial='🟡')
FONT = "font-family=\"'Segoe UI', 'Helvetica Neue', Helvetica, Arial, sans-serif\""


def readme_name(lang):
    return 'README.md' if lang == 'en' else f'README.{lang}.md'


def wrap(text, width):
    words, lines, cur = text.split(), [], ''
    for w in words:
        if cur and len(cur) + 1 + len(w) > width:
            lines.append(cur)
            cur = w
        else:
            cur = f'{cur} {w}'.strip()
    if cur:
        lines.append(cur)
    return lines


def tspans(lines, x, y, lh, **attrs):
    font = '' if 'font_family' in attrs else FONT
    a = ' '.join(f'{k.replace("_", "-")}="{v}"' for k, v in attrs.items())
    out = [f'<text x="{x}" y="{y}" {font} {a}>']
    for i, line in enumerate(lines):
        out.append(f'<tspan x="{x}" dy="{0 if i == 0 else lh}">{escape(line)}</tspan>')
    out.append('</text>')
    return ''.join(out)


def svg(w, h, body, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{escape(title)}">'
            f'<title>{escape(title)}</title>{body}</svg>\n')


def panel(w, h, title):
    return (f'<rect x="1" y="1" width="{w - 2}" height="{h - 2}" rx="18" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="2"/>'
            + tspans([title], 40, 52, 0, font_size=26, font_weight=700, fill='#0F172A'))


# ----------------------------------------------------------------------------- diagrams
def d_banner(t, cat):
    w, h = 1200, 380
    b = ['<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0F172A"/>'
         '<stop offset="1" stop-color="#1E3A8A"/></linearGradient></defs>',
         f'<rect width="{w}" height="{h}" rx="22" fill="url(#g)"/>',
         '<polygon points="96,58 52,196 100,196 78,322 168,160 116,160 146,58" fill="#FBBF24"/>',
         tspans(['Éclair Skills'], 200, 140, 0, font_size=74, font_weight=800, fill='#FFFFFF'),
         tspans(wrap(t['tagline'], 48), 204, 190, 32, font_size=24, fill='#CBD5E1'),
         tspans([t['banner_sub']], 204, 330, 0, font_size=22, font_weight=700, fill='#FBBF24')]
    counts = {c: sum(1 for s in cat['skills'] if s['category'] == c) for c in ORDER}
    for i, c in enumerate(ORDER):
        x, y = 868 + (i % 6) * 50, 70 + (i // 6) * 50
        b.append(f'<rect x="{x}" y="{y}" width="44" height="44" rx="10" fill="{COLORS[c]}"/>')
        b.append(tspans([str(counts[c])], x + 22, y + 29, 0, font_size=18, font_weight=800, fill='#FFFFFF', text_anchor='middle'))
    b.append(tspans([f'= {len(cat["skills"])}'], 1015, 268, 0, font_size=40, font_weight=800, fill='#FFFFFF', text_anchor='middle'))
    return svg(w, h, ''.join(b), 'Éclair Skills — ' + t['tagline'])


def d_how(t):
    w, h = 1200, 400
    b = [panel(w, h, t['d_how'])]
    cw, gap, x0, y0 = 200, 30, 40, 90
    colors = ['#2563EB', '#7C3AED', '#EA580C', '#0D9488', '#16A34A']
    for i, (title, text) in enumerate(t['steps']):
        x = x0 + i * (cw + gap)
        b.append(f'<rect x="{x}" y="{y0}" width="{cw}" height="220" rx="16" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="2"/>')
        b.append(f'<rect x="{x}" y="{y0}" width="{cw}" height="8" rx="4" fill="{colors[i]}"/>')
        b.append(f'<circle cx="{x + 34}" cy="{y0 + 46}" r="20" fill="{colors[i]}"/>')
        b.append(tspans([str(i + 1)], x + 34, y0 + 54, 0, font_size=20, font_weight=800, fill='#FFFFFF', text_anchor='middle'))
        b.append(tspans([title], x + 62, y0 + 53, 0, font_size=17, font_weight=700, fill='#0F172A'))
        b.append(tspans(wrap(text, 21), x + 18, y0 + 100, 22, font_size=15, fill='#334155'))
        if i < 4:
            ax = x + cw + 4
            b.append(f'<path d="M{ax} {y0 + 110} l20 0 m-8 -8 l8 8 l-8 8" stroke="#94A3B8" stroke-width="3" fill="none" stroke-linecap="round"/>')
    b.append(f'<rect x="{x0}" y="330" width="{5 * cw + 4 * gap}" height="44" rx="12" fill="#DCFCE7"/>')
    b.append(tspans(['✓ ' + t['d_human']], w / 2, 358, 0, font_size=18, font_weight=700, fill='#166534', text_anchor='middle'))
    return svg(w, h, ''.join(b), t['d_how'])


def d_anatomy(t):
    w, h = 1200, 470
    b = [panel(w, h, t['d_anat'])]
    b.append(tspans(['skills/eclair-<name>/'], 40, 92, 0, font_size=18, font_weight=700, fill='#475569', font_family='monospace'))
    # SKILL.md card
    b.append('<rect x="40" y="110" width="540" height="330" rx="16" fill="#FFFFFF" stroke="#2563EB" stroke-width="2"/>')
    b.append('<rect x="40" y="110" width="540" height="48" rx="16" fill="#2563EB"/><rect x="40" y="140" width="540" height="18" fill="#2563EB"/>')
    b.append(tspans(['📄 ' + t['d_skillmd']], 64, 142, 0, font_size=20, font_weight=700, fill='#FFFFFF'))
    for i, sec in enumerate(t['d_anat_sections']):
        y = 190 + i * 36
        b.append(f'<circle cx="76" cy="{y - 6}" r="13" fill="#DBEAFE"/>')
        b.append(tspans([str(i + 1)], 76, y - 1, 0, font_size=14, font_weight=700, fill='#1D4ED8', text_anchor='middle'))
        b.append(tspans([sec], 100, y, 0, font_size=17, fill='#0F172A'))
    # references card
    b.append('<rect x="660" y="110" width="500" height="330" rx="16" fill="#FFFFFF" stroke="#0D9488" stroke-width="2"/>')
    b.append('<rect x="660" y="110" width="500" height="48" rx="16" fill="#0D9488"/><rect x="660" y="140" width="500" height="18" fill="#0D9488"/>')
    b.append(tspans(['📁 ' + t['d_refs']], 684, 142, 0, font_size=20, font_weight=700, fill='#FFFFFF'))
    for i, (name, desc) in enumerate(t['d_anat_refs']):
        y = 200 + i * 60
        b.append(f'<rect x="684" y="{y - 26}" width="452" height="50" rx="10" fill="#F0FDFA"/>')
        b.append(tspans([name], 700, y - 4, 0, font_size=16, font_weight=700, fill='#115E59', font_family='monospace'))
        b.append(tspans([desc], 700, y + 16, 0, font_size=15, fill='#334155'))
    b.append('<path d="M584 262 L652 262 m-10 -10 l10 10 l-10 10" stroke="#0D9488" stroke-width="3" fill="none" stroke-linecap="round"/>')
    return svg(w, h, ''.join(b), t['d_anat'])


def d_assemble(t, cat, lang):
    w, h = 1200, 590
    b = [panel(w, h, t['d_asm'])]
    counts = {c: sum(1 for s in cat['skills'] if s['category'] == c) for c in ORDER}
    labels = LAYER_LABELS[LANGS.index(lang)]
    b.append(f'<rect x="40" y="84" width="{w - 80}" height="50" rx="12" fill="#16A34A"/>')
    b.append(tspans(['🌐 ' + t['d_site']], w / 2, 116, 0, font_size=20, font_weight=700, fill='#FFFFFF', text_anchor='middle'))
    x0, avail, gap, rh = 170, w - 40 - 170, 10, 82
    for r, row in enumerate(LAYERS):
        y = 148 + r * (rh + 10)
        b.append(f'<rect x="40" y="{y}" width="120" height="{rh}" rx="12" fill="#E2E8F0"/>')
        b.append(tspans([labels[r]], 100, y + rh / 2 + 6, 0, font_size=17, font_weight=700, fill='#0F172A', text_anchor='middle'))
        bw = (avail - gap * (len(row) - 1)) / len(row)
        chars = max(10, int((bw - 24) / 7.8))
        for i, c in enumerate(row):
            x = x0 + i * (bw + gap)
            b.append(f'<rect x="{x:.1f}" y="{y}" width="{bw:.1f}" height="{rh}" rx="12" fill="{COLORS[c]}"/>')
            b.append(tspans([str(counts[c])], x + 12, y + 29, 0, font_size=24, font_weight=800, fill='#FFFFFF'))
            b.append(tspans(wrap(t['fam'][c][0], chars)[:3], x + 12, y + 48, 15, font_size=13, font_weight=700, fill='#FFFFFF'))
    y = 148 + len(LAYERS) * (rh + 10)
    b.append(f'<rect x="40" y="{y}" width="{w - 80}" height="56" rx="12" fill="#0F172A"/>')
    b.append(tspans(['🔒 ' + t['d_core']], w / 2, y + 35, 0, font_size=20, font_weight=700, fill='#FFFFFF', text_anchor='middle'))
    return svg(w, h, ''.join(b), t['d_asm'])


def d_families(t, cat):
    cols, tw, th, gap = 6, 177, 112, 11
    rows = -(-len(ORDER) // cols)
    w, h = 1200, 84 + rows * (th + gap) + 14
    b = [panel(w, h, t['families_title'])]
    counts = {c: sum(1 for s in cat['skills'] if s['category'] == c) for c in ORDER}
    for i, c in enumerate(ORDER):
        x, y = 40 + (i % cols) * (tw + gap), 80 + (i // cols) * (th + gap)
        b.append(f'<rect x="{x}" y="{y}" width="{tw}" height="{th}" rx="14" fill="{COLORS[c]}"/>')
        b.append(tspans([str(counts[c])], x + 16, y + 40, 0, font_size=30, font_weight=800, fill='#FFFFFF'))
        b.append(tspans(wrap(t['fam'][c][0], 19)[:3], x + 16, y + 64, 18, font_size=15, font_weight=700, fill='#FFFFFF'))
    return svg(w, h, ''.join(b), t['families_title'])


def d_maturity(t):
    w, h = 1200, 440
    b = [panel(w, h, t['d_mat'])]
    colors = ['#16A34A', '#2563EB', '#EA580C', '#7C3AED']
    bw = 262
    for i, (title, text) in enumerate(t['levels']):
        x = 40 + i * (bw + 18)
        top = 230 - i * 40
        b.append(f'<rect x="{x}" y="{top}" width="{bw}" height="{410 - top}" rx="14" fill="{colors[i]}"/>')
        b.append(tspans([f'{i + 1}. {title}'], x + 18, top + 34, 0, font_size=20, font_weight=800, fill='#FFFFFF'))
        b.append(tspans(wrap(text, 30)[:5], x + 18, top + 62, 19, font_size=14, fill='#F8FAFC'))
    b.append('<rect x="40" y="140" width="262" height="44" rx="22" fill="#FEF9C3" stroke="#CA8A04" stroke-width="2"/>')
    b.append(tspans([f'📍 {t["d_here"]} — {t["here"]}'], 171, 168, 0, font_size=16, font_weight=700, fill='#713F12', text_anchor='middle'))
    b.append('<path d="M171 186 L171 226" stroke="#CA8A04" stroke-width="3" stroke-dasharray="6 5"/>')
    return svg(w, h, ''.join(b), t['d_mat'])


# ----------------------------------------------------------------------------- README
def lang_bar(cur):
    parts = []
    for lang in LANGS:
        name = T[lang]['lang_name']
        parts.append(f'<b>{name}</b>' if lang == cur else f'<a href="{readme_name(lang)}">{name}</a>')
    return ' · '.join(parts)


def skill_link(name):
    return f'[`{name}`](skills/{name}/SKILL.md)'


def readme(lang, cat):
    t = T[lang]
    li = LANGS.index(lang)
    a = f'docs/assets/{lang}'
    by = {c: [s for s in cat['skills'] if s['category'] == c] for c in ORDER}
    L = []
    add = L.append
    add('<!-- Generated by scripts/build_readmes.py — edit scripts/readme_data_*.py, not this file. -->')
    add('<a id="top"></a>\n')
    add(f'<p align="center"><img src="{a}/banner.svg" alt="Éclair Skills — {escape(t["tagline"])}" width="100%"></p>\n')
    add(f'<p align="center">{lang_bar(lang)}</p>\n')
    add('<p align="center">'
        f'<a href="{REPO}/actions/workflows/validate.yml"><img src="{REPO}/actions/workflows/validate.yml/badge.svg" alt="CI"></a> '
        '<img src="https://img.shields.io/badge/skills-{n}-F59E0B" alt="{n} skills">'.format(n=len(cat['skills'])) + ' '
        '<img src="https://img.shields.io/badge/Éclair%20CMS-2.0.x-1E3A8A" alt="Éclair CMS 2.0.x"> '
        '<img src="https://img.shields.io/badge/contract-eclair--extension%2F1-0D9488" alt="eclair-extension/1"> '
        '<a href="LICENSE"><img src="https://img.shields.io/badge/license-AGPL--3.0--only-475569" alt="AGPL-3.0-only"></a>'
        '</p>\n')
    add(t['intro'] + '\n')
    add(f'> [!IMPORTANT]\n> **{t["notice_title"]}** — {t["notice"]}\n')

    add(f'## {t["why_title"]}\n')
    for bold, text in t['why']:
        add(f'- **{bold}** — {text}')
    add('')

    add(f'## {t["how_title"]}\n')
    add(f'<p align="center"><img src="{a}/how-it-works.svg" alt="{escape(t["d_how"])}" width="100%"></p>\n')
    add(t['how_intro'] + '\n')
    for i, (title, text) in enumerate(t['steps'], 1):
        add(f'{i}. **{title}** — {text}')
    add('')

    add(f'## {t["anatomy_title"]}\n')
    add(f'<p align="center"><img src="{a}/skill-anatomy.svg" alt="{escape(t["d_anat"])}" width="100%"></p>\n')
    add(t['anatomy_intro'] + '\n')
    add('```text\nskills/eclair-commerce-pro/\n├── SKILL.md\n└── references/\n    ├── core-map.md\n    ├── native-contract.md\n    ├── family-contract.md\n    └── acceptance.md\n```\n')
    add(f'| {t["col_part"]} | {t["col_role"]} |\n|---|---|')
    for part, role in t['anatomy_rows']:
        add(f'| {part} | {role} |')
    add('')

    add(f'## {t["assemble_title"]}\n')
    add(f'<p align="center"><img src="{a}/how-skills-fit.svg" alt="{escape(t["d_asm"])}" width="100%"></p>\n')
    add(t['assemble_intro'] + '\n')
    for i, (title, text) in enumerate(t['layers'], 1):
        add(f'{i}. **{title}** — {text}')
    add('')

    add(f'## {t["families_title"]}\n')
    add(f'<p align="center"><img src="{a}/families.svg" alt="{escape(t["families_title"])}" width="100%"></p>\n')
    add(f'| | {COL_FAM[lang][0]} | {COL_FAM[lang][1]} | Skills |\n|---|---|---|---:|')
    for c in ORDER:
        add(f'| {EMOJI[c]} | **{t["fam"][c][0]}** | {t["fam"][c][1]} | {len(by[c])} |')
    add(f'| | | | **{len(cat["skills"])}** |\n')

    wp = WORDPRESS[li]
    add(f'## {wp[0]}\n')
    add(wp[1] + '\n')
    add(f'| {wp[2]} | {wp[3]} |\n|---|---:|')
    for m in MAT_ORDER:
        n = sum(1 for s in cat['skills'] if MATURITY[s['maturity']] == m)
        add(f'| {MAT_ICON[m]} {t["mat"][m]} | {n} |')
    add('')
    add(wp[4] + '\n')

    add(f'## {t["quick_title"]}\n')
    add(t['q_req'] + '\n')
    add(f'**1. {t["q_clone"]}**\n')
    add(f'```bash\ngit clone {REPO}.git\ncd eclair-skills\npython3 scripts/validate_skills.py\n```\n')
    add(f'**2. {t["q_list"]}**\n')
    add('```bash\npython3 scripts/install_skills.py --list\n```\n')
    add(f'**3. {t["q_install"]}**\n')
    add('```bash\n'
        f'python3 scripts/install_skills.py --project /path/to/my-site --category commerce   {t["cmt_family"]}\n'
        f'python3 scripts/install_skills.py --project /path/to/my-site --skill eclair-wordpress-migration   {t["cmt_skill"]}\n'
        f'python3 scripts/install_skills.py --project /path/to/my-site --all   {t["cmt_all"]}\n'
        '```\n')
    add(t['q_install_note'] + '\n')
    add(f'**4. {t["q_agent"]}**\n')
    for p in t['prompts']:
        add(f'> {p}\n')
    add(t['q_agent_note'] + '\n')

    add(f'## {t["recipes_title"]}\n')
    add(t['recipes_intro'] + '\n')
    for title, skills in t['recipes']:
        add(f'**{title}**\n')
        add(' → '.join(skill_link(s) for s in skills) + '\n')

    add(f'## {t["catalog_title"]}\n')
    add(t['catalog_intro'] + '\n')
    add(t['legend'] + '\n')
    for c in ORDER:
        add(f'<details{" open" if c == ORDER[0] else ""}>\n<summary><b>{EMOJI[c]} {t["fam"][c][0]} ({len(by[c])})</b> — {t["fam"][c][1]}</summary>\n')
        add(f'| {t["col_skill"]} | {t["col_what"]} | {t["col_status"]} |\n|---|---|---|')
        for s in by[c]:
            m = MATURITY[s['maturity']]
            add(f'| {skill_link(s["name"])} | {SKILLS[s["name"]][li]} | {MAT_ICON[m]} {t["mat"][m]} |')
        add('\n</details>\n')

    add(f'## {t["maturity_title"]}\n')
    add(f'<p align="center"><img src="{a}/maturity.svg" alt="{escape(t["d_mat"])}" width="100%"></p>\n')
    add(t['maturity_intro'] + '\n')
    for i, (title, text) in enumerate(t['levels'], 1):
        add(f'{i}. **{title}** — {text}')
    add('')
    add(f'> [!WARNING]\n> {t["gates_note"]}\n')

    add(f'## {t["examples_title"]}\n')
    add(f'| {t["col_path"]} | {t["col_state"]} | {t["col_desc"]} |\n|---|---|---|')
    for path, state, desc in t['examples']:
        add(f'| [`{path}`]({path}) | {state} | {desc} |')
    add('')
    add(f'**{t["demo_title"]}**\n')
    add('```bash\n# in a checkout of https://github.com/Jacckisback/eclair-cms\n'
        'php tools/validate.php /path/to/eclair-skills/examples/extensions/catalogue-demo --json\n'
        'php tests/run.php\nphp tools/measure.php --check\n```\n')

    add(f'## {t["quality_title"]}\n')
    add(t['quality_intro'] + '\n')
    add('```bash\npython3 scripts/validate_skills.py\npython3 scripts/check_release.py\npython3 scripts/verify_sample.py\n'
        'python3 scripts/verify_member_directory.py\npython3 -m unittest discover -s tests -p \'test_*.py\' -v\n'
        'php -l examples/extensions/catalogue-demo/extension.php\nphp tests/member-directory.php\n'
        'php tests/member-public.php\nphp tests/member-enroll.php\n```\n')
    add(t['ci_note'] + '\n')
    add(f'### 🔏 {t["sig_title"]}\n')
    add(t['sig_text'] + '\n')
    add('```bash\nphp scripts/verify_signature.php\n```\n')
    add(t['sig_after'] + '\n')

    add(f'## {t["limits_title"]}\n')
    for x in t['limits']:
        add(f'- {x}')
    add('')
    add(f'## {t["compat_title"]}\n')
    for x in t['compat']:
        add(f'- {x}')
    add('')
    add(f'## {t["more_title"]}\n')
    for path, label in t['more']:
        add(f'- [{label}]({path})')
    add('')
    add(f'## {t["license_title"]}\n')
    add(t['license_text'] + '\n')
    add('---\n')
    add(f'<p align="center">{lang_bar(lang)} · <a href="#top">{t["nav_top"]} ↑</a></p>')
    return '\n'.join(L) + '\n'


def catalogue_doc(cat):
    t = T['fr']
    n = len(cat['skills'])
    L = [f'# Catalogue complet — Éclair Skills v{cat["catalog_version"]}', '',
         f'Généré par `scripts/build_readmes.py` à partir de `catalog.json`. **{n} Agent Skills = {n} guides pour agents, pas {n} extensions PHP.** Cible : Éclair CMS 2.0.x, contrat `eclair-extension/1`.', '',
         t['legend'], '']
    for c in ORDER:
        rows = [s for s in cat['skills'] if s['category'] == c]
        L += [f'## {EMOJI[c]} {t["fam"][c][0]} ({len(rows)})', '', f'{t["fam"][c][1]}.', '',
              '| Skill | Ce qu’il aide l’agent à faire | Équivalent WordPress | Statut |', '|---|---|---|---|']
        for s in rows:
            m = MATURITY[s['maturity']]
            L.append(f'| [`{s["name"]}`](../skills/{s["name"]}/SKILL.md) | {SKILLS[s["name"]][1]} | {WP_EQUIV.get(s["name"], "—")} | {MAT_ICON[m]} {t["mat"][m]} |')
        L.append('')
    L.append(f'**Total : {n} skills.**')
    return '\n'.join(L) + '\n'


def outputs():
    cat = json.loads((ROOT / 'catalog.json').read_text(encoding='utf-8'))
    names = [s['name'] for s in cat['skills']]
    missing = sorted(set(names) - set(SKILLS)) + sorted(set(SKILLS) - set(names))
    if missing:
        raise SystemExit(f'readme_data_skills.py out of sync with catalog.json: {missing}')
    files = {'docs/CATALOGUE_COMPLET.md': catalogue_doc(cat)}
    for lang in LANGS:
        t = T[lang]
        a = f'docs/assets/{lang}'
        files[f'{a}/banner.svg'] = d_banner(t, cat)
        files[f'{a}/how-it-works.svg'] = d_how(t)
        files[f'{a}/skill-anatomy.svg'] = d_anatomy(t)
        files[f'{a}/how-skills-fit.svg'] = d_assemble(t, cat, lang)
        files[f'{a}/families.svg'] = d_families(t, cat)
        files[f'{a}/maturity.svg'] = d_maturity(t)
        files[readme_name(lang)] = readme(lang, cat)
    return files


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true', help='fail if generated files are out of date')
    args = ap.parse_args()
    files = outputs()
    stale = []
    for rel, content in files.items():
        p = ROOT / rel
        if args.check:
            if not p.is_file() or p.read_text(encoding='utf-8') != content:
                stale.append(rel)
        else:
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(content, encoding='utf-8')
    if args.check:
        if stale:
            print('FAIL: regenerate with python3 scripts/build_readmes.py:\n- ' + '\n- '.join(stale))
            return 1
        print(f'PASS: {len(files)} generated README/diagram files are up to date')
        return 0
    print(f'WROTE {len(files)} files ({len(LANGS)} README + {len(files) - len(LANGS)} SVG)')
    return 0


if __name__ == '__main__':
    sys.exit(main())
