#!/usr/bin/env python3
"""Generate the catalogue-driven skills in every language and keep shared references in sync.

    python3 scripts/build_skills.py                  # write everything
    python3 scripts/build_skills.py --check          # fail if anything is out of date
    python3 scripts/build_skills.py --export-source DIR   # French source chunks for translators

Sources
- scripts/skill_specs_*.py and scripts/skill_specs_legacy.json: French fields of each skill.
- i18n/fr/templates.json: French skeletons and shared sentences.
- i18n/<lang>/templates.json and i18n/<lang>/skills_*.json: translations (en, es, de, it, pt).

Outputs
- skills/<name>/                 French (default language, source of truth)
- translations/<lang>/<name>/    the same skill in another language
- catalog.json                   names, families, maturity

The eight foundation skills are hand-written: only their shared references/core-map.md is
generated here; their translations live as plain files under translations/<lang>/.
Standard library only.
"""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import skill_specs_a, skill_specs_b, skill_specs_c  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
VERSION = '2.2.0'
LANGS = ('fr', 'en', 'es', 'de', 'it', 'pt')
TRANSLATED = LANGS[1:]

# Family order; French titles and scopes of the families added in 2.1 (older ones live in catalog.json).
ORDER = ['foundation', 'content', 'media', 'components', 'design', 'multilingual', 'forms', 'seo', 'marketing',
         'commerce', 'lms', 'community', 'business', 'integrations', 'performance', 'security', 'admin', 'developer']
NEW_GROUPS = {
    'content': ('Contenu et édition', 'Articles, pages, catégories, menus, recherche, flux'),
    'media': ('Médias', 'Médiathèque, images, galeries, vidéo, audio, documents'),
    'components': ('Blocs et composants', 'FAQ, onglets, tableaux, tarifs, sections, navigation'),
    'multilingual': ('Multilingue', 'Langues, sélecteur, formats, adresses, traduction'),
    'forms': ('Formulaires', 'Contact, devis, étapes, pièces jointes, sondages, calculs'),
    'marketing': ('Marketing et audience', 'Newsletter, pages d\'atterrissage, mesure, partage, publicité'),
    'performance': ('Performance', 'Cache, CDN, images, poids, signaux web essentiels'),
    'security': ('Sécurité et confidentialité', 'Connexion, 2FA, spam, en-têtes, intégrité, données personnelles'),
    'admin': ('Administration et maintenance', 'Comptes, sauvegardes, mises à jour, déménagement, journal'),
    'developer': ('Développement et outils', 'API en lecture, Markdown, MCP, ligne de commande, portage'),
}
MATURITY = {
    'C': 'core-builtin-configuration-workflow',
    'N': 'native-v2-workflow',
    'R': 'public-read-only-prototype-possible',
    'D': 'design-workflow-requires-verified-core-capabilities',
    'P': 'partly-blocked-by-core-contract',
}
FIELDS = ('name', 'mat', 'title', 'goal', 'wp', 'model', 'procedure', 'invariant', 'pos', 'neg', 'en', 'es', 'de', 'it', 'pt')
TEXT_FIELDS = ('title', 'goal', 'wp', 'model', 'procedure', 'invariant', 'pos', 'neg')
DESC_FRAME = ("{one_liner} Use on Éclair CMS 2.x when the user wants to: {goal}. "
              "Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin.")


def specs():
    """Skills generated since 2.1, by family (French fields + one-line catalogue descriptions)."""
    out = {}
    for mod in (skill_specs_a, skill_specs_b, skill_specs_c):
        for cat, rows in mod.SPECS.items():
            for row in rows:
                if len(row) != len(FIELDS):
                    raise SystemExit(f'Bad spec row in {cat}: {row[0]} ({len(row)} fields)')
                out.setdefault(cat, []).append(dict(zip(FIELDS, row)))
    return out


def legacy():
    """The 49 template skills of 2.0, by family (French fields)."""
    return json.loads((ROOT / 'scripts/skill_specs_legacy.json').read_text(encoding='utf-8'))


def one_liners():
    """name -> {lang: one-line description} for every templated skill."""
    from readme_data_skills import LANGS as RL, SKILLS
    out = {name: dict(zip(RL, vals)) for name, vals in SKILLS.items()}
    for rows in specs().values():
        for s in rows:
            out[s['name']] = {'en': s['en'], 'fr': s['goal'][0].upper() + s['goal'][1:] + '.',
                              'es': s['es'], 'de': s['de'], 'it': s['it'], 'pt': s['pt']}
    return out


def family_titles():
    """family -> {lang: title}."""
    from readme_data_text import T
    from readme_data_families import FAMILIES
    order = ('en', 'fr', 'es', 'de', 'it', 'pt')
    out = {k: {lang: T[lang]['fam'][k][0] for lang in order} for k in T['en']['fam']}
    for k, names in FAMILIES.items():
        out[k] = {lang: names[i][0] for i, lang in enumerate(order)}
    return out


def fill(tpl, **kw):
    for k, v in kw.items():
        tpl = tpl.replace('{' + k + '}', v)
    return tpl


def load_lang(lang):
    """Templates and per-skill text fields of one language, or None if not translated yet."""
    d = ROOT / 'i18n' / lang
    tp = d / 'templates.json'
    if not tp.is_file() or (lang != 'fr' and not (d / 'foundation').is_dir()):
        return None
    tpl = json.loads(tp.read_text(encoding='utf-8'))
    fields = {}
    if lang != 'fr':
        for f in sorted(d.glob('skills_*.json')):
            fields.update(json.loads(f.read_text(encoding='utf-8')))
    return tpl, fields


def all_templated():
    """[(family, spec, is_legacy)] in catalogue order."""
    gen, leg = specs(), legacy()
    out = []
    for key in ORDER:
        out += [(key, s, True) for s in leg.get(key, [])]
        out += [(key, s, False) for s in gen.get(key, [])]
    return out


def render(lang, tpl, family, s, text, is_legacy, liners, fam_titles):
    m = s['mat']
    fam = fam_titles[family][lang]
    contract = tpl['family_line'][family] if is_legacy else tpl['contract'][m]
    # French keeps the English one-liner so the description triggers in both languages.
    one = liners[s['name']]['en' if lang == 'fr' else lang]
    desc = fill(DESC_FRAME, one_liner=one, goal=text['goal']).replace('"', "'")
    common = dict(name=s['name'], title=text['title'], goal=text['goal'], model=text['model'], procedure=text['procedure'],
                  invariant=text['invariant'], pos=text['pos'], neg=text['neg'], contract=contract, family=fam)
    return {
        'SKILL.md': fill(tpl['skill_md'], description=desc, status=tpl['status'][m], deliverable=tpl['deliverable'][m],
                         maturity=MATURITY[m], wp_line=fill(tpl['wp_line'], wp=text['wp'], family=fam), **common),
        'references/native-contract.md': fill(tpl['native_contract'], **common),
        'references/family-contract.md': fill(tpl['family_contract'], family=fam, limitation=tpl['limitation'][family]),
        'references/acceptance.md': fill(tpl['acceptance'], **common),
        'references/core-map.md': tpl['core_map'],
    }


def outputs():
    cat = json.loads((ROOT / 'catalog.json').read_text(encoding='utf-8'))
    templated = all_templated()
    names = [s['name'] for _f, s, _l in templated]
    if len(set(names)) != len(names):
        raise SystemExit('Duplicate skill names between specs')
    foundation = [s for s in cat['skills'] if s['category'] == 'foundation']
    groups = dict(cat['groups'])
    for key, (title, desc) in NEW_GROUPS.items():
        groups.setdefault(key, {})
        groups[key].update(title=title, description=desc)
    skills = list(foundation) + [{'name': s['name'], 'category': f, 'maturity': MATURITY[s['mat']], 'kind': 'agent-skill'}
                                 for f, s, _l in templated]
    for key in ORDER:
        groups[key]['count'] = sum(1 for s in skills if s['category'] == key)
    cat['groups'] = {k: groups[k] for k in ORDER}
    cat['skills'] = skills
    cat['catalog_version'] = VERSION
    cat['languages'] = {'default': 'fr', 'translations': [lang for lang in TRANSLATED if load_lang(lang)]}
    cat['generated_for'] = 'wordpress-alternative-catalogue'
    cat['status'] = 'workflow-library-core-builtin-and-native-usable-transactional-modules-design-only'
    cat['notes'] = [
        f'All {len(skills)} entries are agent skills (guides), not {len(skills)} working PHP plugins.',
        'Maturity core-builtin-configuration-workflow: the feature already exists in the Éclair core; the skill configures and checks it.',
        'Extensions expose public GET routes only on Éclair 2.0; public POST (PR #19) is a draft, not merged.',
        'skills/ is French (source); translations/<lang>/ holds the same skills in en, es, de, it, pt.',
        'Catalogue demo is a read-only example, no commerce transactions.',
    ]
    files = {'catalog.json': json.dumps(cat, indent=2, ensure_ascii=False) + '\n'}
    liners, fam_titles = one_liners(), family_titles()
    for lang in LANGS:
        loaded = load_lang(lang)
        if loaded is None:
            continue
        tpl, fields = loaded
        base = 'skills' if lang == 'fr' else f'translations/{lang}'
        for s in foundation:
            files[f"{base}/{s['name']}/references/core-map.md"] = tpl['core_map']
        if lang != 'fr':
            # Hand-written foundation skills: translated files, deduplicated in i18n/<lang>/foundation/.
            fmap = json.loads((ROOT / 'i18n/foundation-map.json').read_text(encoding='utf-8'))
            for path, key in fmap.items():
                src = ROOT / 'i18n' / lang / 'foundation' / key
                if not src.is_file():
                    raise SystemExit(f'i18n/{lang}/foundation: missing {key}')
                files[f'{base}/{path}'] = src.read_text(encoding='utf-8')
            # Data assets of the foundation skills (CSV, JSON examples) are copied as they are.
            for s in foundation:
                for f in sorted((ROOT / 'skills' / s['name']).rglob('*')):
                    if f.is_file() and f.suffix != '.md':
                        files[f"{base}/{s['name']}/{f.relative_to(ROOT / 'skills' / s['name']).as_posix()}"] = f.read_text(encoding='utf-8')
        for family, s, is_legacy in templated:
            if lang == 'fr':
                text = {k: s[k] for k in TEXT_FIELDS}
            else:
                text = fields.get(s['name'])
                if not text or any(not str(text.get(k, '')).strip() for k in TEXT_FIELDS):
                    raise SystemExit(f'i18n/{lang}: missing or incomplete translation for {s["name"]}')
            for rel, content in render(lang, tpl, family, s, text, is_legacy, liners, fam_titles).items():
                files[f"{base}/{s['name']}/{rel}"] = content
    return files


def export_source(dest, chunks=2):
    """Write the French fields to translate, split into chunks keyed by skill name."""
    dest.mkdir(parents=True, exist_ok=True)
    rows = [s for _f, s, _l in all_templated()]
    size = -(-len(rows) // chunks)
    for i in range(chunks):
        part = {s['name']: {k: s[k] for k in TEXT_FIELDS} for s in rows[i * size:(i + 1) * size]}
        (dest / f'skills_{i + 1}.json').write_text(json.dumps(part, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    print(f'Exported {len(rows)} skills in {chunks} chunks to {dest}')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true')
    ap.add_argument('--export-source', type=Path)
    args = ap.parse_args()
    if args.export_source:
        export_source(args.export_source)
        return 0
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
            print('FAIL: regenerate with python3 scripts/build_skills.py:\n- ' + '\n- '.join(stale[:20]))
            return 1
        print(f'PASS: {len(files)} generated skill files are up to date')
        return 0
    print(f'WROTE {len(files)} files')
    return 0


if __name__ == '__main__':
    sys.exit(main())
