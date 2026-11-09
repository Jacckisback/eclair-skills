#!/usr/bin/env python3
"""Generate the catalogue-driven skills and keep shared references in sync.

    python3 scripts/build_skills.py          # write generated skills, core-map.md, catalog.json
    python3 scripts/build_skills.py --check  # fail if anything is out of date

- Skills listed in scripts/skill_specs_*.py are fully generated (SKILL.md + references/).
- The original hand-written skills are never regenerated; only their shared
  references/core-map.md is synchronised, so every skill sees the same core snapshot.
- catalog.json is the single source of truth for names, families and maturity.
Standard library only.
"""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import skill_specs_a, skill_specs_b, skill_specs_c  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
VERSION = '2.1.0'
CORE_COMMIT = '6567d7642ea2227a598c4988e970d43e2e5e0e4f'
CORE_DATE = '9 novembre 2026'

# Family order and French metadata (existing families keep their catalog.json titles).
ORDER = ['foundation', 'content', 'media', 'components', 'design', 'multilingual', 'forms', 'seo', 'marketing',
         'commerce', 'lms', 'community', 'business', 'integrations', 'performance', 'security', 'admin', 'developer']
NEW_GROUPS = {
    'content': ('Contenu et édition', 'Articles, pages, catégories, menus, recherche, flux',
                "Les contenus et leur publication passent par l'administration ou le connecteur MCP, en brouillon ; les types de contenu personnalisés et les écritures de visiteurs (commentaires) ne sont pas ouverts aux extensions en 2.0."),
    'media': ('Médias', 'Médiathèque, images, galeries, vidéo, audio, documents',
              "Le noyau optimise et ré-encode les images ; tout lecteur ou visionneuse tiers se heurte à la politique de contenu native ; les fichiers privés ou payants ne peuvent pas être servis par une adresse publique."),
    'components': ('Blocs et composants', 'FAQ, onglets, tableaux, tarifs, sections, navigation',
                   "Les blocs du noyau couvrent l'essentiel ; un bloc supplémentaire passe par une extension déclarant ses champs ; l'apparence passe par un thème de site, jamais par une modification du noyau."),
    'multilingual': ('Multilingue', 'Langues, sélecteur, formats, adresses, traduction',
                     "Les langues du site public sont celles prises en charge par le noyau (à lire dans les capacités) ; la liaison fine entre versions et la traduction des adresses dépendent du contrat du noyau."),
    'forms': ('Formulaires', 'Contact, devis, étapes, pièces jointes, sondages, calculs',
              "Seul le formulaire de contact natif reçoit des envois de visiteurs en 2.0 ; tout autre formulaire avec envoi au serveur exige une route POST publique non ouverte aux extensions."),
    'marketing': ('Marketing et audience', 'Newsletter, pages d\'atterrissage, mesure, partage, publicité',
                  "Affiliation et publicité sont natives ; inscriptions, campagnes et scripts de mesure tiers dépendent d'un service externe, du consentement et de la politique de contenu native."),
    'performance': ('Performance', 'Cache, CDN, images, poids, signaux web essentiels',
                    "Cache statique, images responsives et script unique sont natifs ; le travail consiste à ne pas les dégrader et à mesurer, jamais à promettre un score."),
    'security': ('Sécurité et confidentialité', 'Connexion, 2FA, spam, en-têtes, intégrité, données personnelles',
                 "Les protections sont natives et ne doivent jamais être relâchées ; un skill ne lit, n'affiche et ne déplace aucun secret ; toute exception passe par la personne responsable."),
    'admin': ('Administration et maintenance', 'Comptes, sauvegardes, mises à jour, déménagement, journal',
              "Sauvegarde, restauration, mise à jour signée et journal sont natifs ; les actions sensibles exigent le droit Sécurité et le mot de passe de la personne, jamais d'un agent seul."),
    'developer': ('Développement et outils', 'API en lecture, Markdown, MCP, ligne de commande, portage',
                  "Les extensions n'ouvrent que des routes GET publiques et des pages d'administration protégées ; pas de filtre de rendu, pas d'API d'écriture publique en 2.0."),
}
MATURITY = {
    'C': 'core-builtin-configuration-workflow',
    'N': 'native-v2-workflow',
    'R': 'public-read-only-prototype-possible',
    'D': 'design-workflow-requires-verified-core-capabilities',
    'P': 'partly-blocked-by-core-contract',
}
STATUS = {
    'C': "Cette fonction est **déjà intégrée au noyau Éclair 2.0** : le skill guide sa configuration et sa vérification, sans écrire d'extension.",
    'N': "Cette fonction est **réalisable aujourd'hui** avec le contrat natif (thème, blocs, routes GET, pages d'administration, tâches).",
    'R': "La **partie publique en lecture est réalisable aujourd'hui** ; les écritures par les visiteurs demandent davantage que le contrat actuel.",
    'D': "Cette fonction **exige des capacités absentes du noyau 2.0** : le skill livre conception, maquette sûre et tests, pas une mise en production.",
    'P': "Cette fonction est **en partie bloquée par le contrat du noyau** : le skill livre ce qui est natif et documente l'écart.",
}
CONTRACT = {
    'C': "La fonction existe dans le noyau : la régler par l'administration ou, en brouillon, par le connecteur MCP. Ne pas la dupliquer dans une extension et ne jamais modifier le noyau pour l'adapter ; si un besoin dépasse ce que le noyau offre, le signaler comme un écart.",
    'N': "Réalisable avec `eclair-extension/1` et le contrat de thème : routes GET publiques cacheables, pages d'administration protégées, blocs et réglages déclaratifs, tâches planifiées, actifs. Vérifier d'abord qu'un bloc ou un réglage natif ne suffit pas.",
    'R': "La lecture publique (GET, cacheable) est réalisable aujourd'hui. Toute écriture par un visiteur exige une route POST publique que le noyau 2.0 n'ouvre pas aux extensions (PR #19 en brouillon, non fusionnée) : ne pas la simuler.",
    'D': "Cette fonction demande des écritures de visiteurs, des comptes publics, des transactions ou des événements signés que `eclair-extension/1` ne fournit pas en 2.0. Livrer la conception, une maquette GET sûre et des tests bloquants ; ne jamais annoncer une mise en production.",
    'P': "Une partie dépend d'un point d'accroche absent du contrat 2.0 (types de contenu, contribution SEO ou JSON-LD, politique de contenu par fonction, filtre de rendu). Livrer la partie native et documenter précisément l'écart, sans contournement.",
}
DELIVERABLE = {
    'C': "- Réglages et contenus préparés par l'administration ou en brouillon par le MCP ; **aucune extension** tant que le natif suffit.",
    'N': "- Paquet `extension.json`/`extension.php` ou paquet de thème validé, seulement si un bloc ou un réglage natif ne suffit pas.",
    'R': "- Paquet en lecture seule (routes GET) validé, et plan écrit pour la partie en écriture, clairement marquée non livrée.",
    'D': "- Dossier de conception, maquette GET sûre si utile, tests bloquants et demande d'évolution du noyau ; **pas de paquet de production**.",
    'P': "- Paquet ou réglages pour la partie native, et note d'écart précise pour la partie bloquée.",
}

CORE_MAP = f"""# Éclair CMS 2.0.x — carte du noyau vérifiée

Référence : dépôt public `Jacckisback/eclair-cms`, branche `main` vérifiée le {CORE_DATE}, commit de référence `{CORE_COMMIT}`. **Un agent doit toujours revérifier le checkout réel et `GET /<admin>/api/capabilities`** : cette note est un instantané, non une garantie de compatibilité future.

## 1. Déjà intégré au noyau : configurer, ne pas reconstruire

Avant d'écrire la moindre extension, vérifier si le besoin est couvert nativement :

- **Contenus** : pages et articles en blocs, catégories, menus, auteurs, brouillons, planning éditorial ; blocs `paragraph`, `heading`, `list`, `quote`, `image`, `video`, `table`, `code`, `button`, `callout`, `divider`, `hero`, `features`, `faq`, `team`, `contact`.
- **Médias** : images redimensionnées, ré-encodées et converties en WebP responsive, dimensions explicites, chargement différé.
- **Formulaire de contact** et boîte de réception des messages (droit `messages`).
- **SEO et GEO** : titres et descriptions avec analyse en direct, JSON-LD (organisation ou entreprise locale, article, FAQ, fil d'Ariane), sitemap avec images et `hreflang`, flux RSS, Open Graph avec image de partage, redirections 301 et gestionnaire de redirections, IndexNow, `llms.txt`, version Markdown de chaque page, politique pour les robots d'IA.
- **Vitesse** : cache statique de chaque page publique, CSS intégré, un seul script public, aucun cookie public.
- **Sécurité** : double authentification, limites de tentatives, Content-Security-Policy stricte, contenus assainis, contrôle d'intégrité, journal, mises à jour signées avec retour arrière.
- **Sauvegardes** : téléchargement et envoi planifié vers un stockage distant, restauration.
- **Boutique légère** : fiches produit, variantes, catégories, liens de paiement d'un prestataire, flux marchand ; **pas de panier, de commande ni de compte client**.
- **Fonctions livrées** : affiliation, publicité, planning, import WordPress, reprise d'un ancien site, suivi des robots d'IA.
- **Assistant IA et connecteur MCP** : brouillons et propositions seulement, jamais de publication ni de suppression.
- **Apparence** : thèmes et directions artistiques, aperçu avant enregistrement.

## 2. Où un skill peut écrire

- Code noyau : `eclair/app/`, `eclair/assets/`, `eclair/index.php` — **ne jamais éditer** pour livrer une fonctionnalité de site.
- Fonctions du site : `site/extensions/<id>/` avec `extension.json`, `extension.php`, `lib/`, `assets/`, `lang/`.
- Thèmes du site : `site/themes/<id>/` avec `theme.json`.
- Données d'une extension : `Eclair\\Store`, préfixe `$ctx['data']` (`data/ext/<id>/`), secrets dans `data/ext/<id>/secrets.php`.
- Contenus et réglages : par l'administration ou le connecteur MCP uniquement.

## 3. Contrat `eclair-extension/1`

- Routes publiques d'une extension : **GET uniquement**, déclarées dans le manifeste, cacheables ou non.
- Administration : GET/POST sous `/<admin>/x/<id>/...`, droits du noyau (`content`, `media`, `menus`, `categories`, `messages`, `redirects`, `settings`, `users`, `security`) et protection CSRF.
- Blocs et réglages déclaratifs validés par le noyau ; tâches planifiées (au plus une fois par heure) ; migrations idempotentes ; actifs publiés.
- Le code d'une extension est **de confiance, sans bac à sable** : l'import et l'activation exigent une personne autorisée.
- Validation : `php tools/validate.php <dossier> --json`, puis `php tests/run.php` et `php tools/measure.php --check` dans un checkout du noyau.

## 4. Limites connues de la 2.0

- Pas de route POST publique pour les extensions (PR #19 en brouillon, non fusionnée), donc pas d'inscription, de commentaire, de commande ou de dépôt par un visiteur hors formulaire de contact natif.
- Pas d'identité publique (client, élève, membre) dans le contrat natif.
- Pas de type de contenu propre à une extension ; pas de contribution SEO ou JSON-LD par extension ; pas de politique de contenu (CSP) par extension ; pas de filtre général de rendu.
- Étiquettes, commentaires et types de contenu personnalisés de WordPress ne sont pas repris par l'import.
- Les anciens prototypes Éclair Devkit v0.x visaient le noyau 1.14 et **ne s'appliquent pas** à la 2.0.

Sources officielles :
- https://github.com/Jacckisback/eclair-cms/blob/main/docs/EXTENSION-CONTRACT.md
- https://github.com/Jacckisback/eclair-cms/blob/main/docs/THEME-CONTRACT.md
- https://github.com/Jacckisback/eclair-cms/blob/main/docs/SKILLS-GUIDE.md
- https://github.com/Jacckisback/eclair-cms/blob/main/docs/ARCHITECTURE-2.md
- https://github.com/Jacckisback/eclair-cms/blob/main/docs/schemas/extension.schema.json
"""

FIELDS = ('name', 'mat', 'title', 'goal', 'wp', 'model', 'procedure', 'invariant', 'pos', 'neg', 'en', 'es', 'de', 'it', 'pt')


def specs():
    """Generated skills by family, in catalogue order."""
    out = {}
    for mod in (skill_specs_a, skill_specs_b, skill_specs_c):
        for cat, rows in mod.SPECS.items():
            for row in rows:
                if len(row) != len(FIELDS):
                    raise SystemExit(f'Bad spec row in {cat}: {row[0]} ({len(row)} fields)')
                out.setdefault(cat, []).append(dict(zip(FIELDS, row)))
    return out


def description(s):
    return (f"{s['en']} Use on Éclair CMS 2.x when the user wants to: {s['goal']}. "
            f"Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin.")


def skill_md(s, family_title):
    m = s['mat']
    return f"""---
name: {s['name']}
description: "{description(s).replace('"', "'")}"
---

# {s['title']} — Éclair CMS 2.x

## Déclencheur et résultat attendu
Utiliser ce skill pour **{s['goal']}**. {STATUS[m]} Ce skill est un **workflow d'agent**, pas une extension PHP fonctionnelle ni une garantie de conformité.

**Équivalent WordPress :** {s['wp']}. Famille : {family_title}.

## Diagnostic obligatoire avant modification
1. Lire `references/core-map.md` (ce que le noyau fait déjà) et `references/native-contract.md` ; vérifier la version réelle du CMS et les capacités dans `GET /<admin>/api/capabilities` (si l'accès est autorisé).
2. Lire `references/family-contract.md` et `references/acceptance.md`. Ne jamais copier l'ancien système de packs v0.x ni du code PHP de WordPress dans Éclair 2.
3. Identifier le modèle de données : **{s['model']}**. Documenter ce qui est public, ce qui est privé et d'où vient chaque donnée.

## Procédure spécifique
4. **Parcours :** {s['procedure']}. Décrire les états et les erreurs avant d'écrire du code.
5. **Emplacements :** code propre au site dans `site/extensions/<id>/`, apparence dans `site/themes/<id>/`, données sous `$ctx['data']`, contenus et réglages par l'administration ou le MCP. Ne jamais éditer `app/`, `assets/`, `index.php` ni l'updater.
6. **Contrat actuel :** {CONTRACT[m]}
7. **Invariant de sécurité :** {s['invariant']}. Vérifier aussi les droits côté serveur, l'échappement avec `e()`, la validation des données et l'absence de secret ou de donnée personnelle dans le HTML public ou un cache partagé.
8. **Preuves :** écrire le test positif « {s['pos']} » et le test de refus « {s['neg']} ». Mesurer les régressions de SEO et de performance, documenter le retour arrière.
9. **Validation native :** `php tools/validate.php <dossier> --json`, `php tests/run.php` et `php tools/measure.php --check` sur un checkout officiel pour tout paquet produit. Pour une partie non prise en charge par le noyau, fournir une note d'écart et un test bloquant, jamais une réussite fictive.

## Livrables obligatoires
- Mini-spécification : objectif, utilisateurs, parcours, états, données, mesures.
- Matrice d'autorisations et de cache : route, méthode, session, visibilité, indexation.
{DELIVERABLE[m]}
- Tests des cas positifs et des refus, procédure de désactivation qui conserve les données, note de compatibilité.

## Critères d'acceptation
- {s['pos']}.
- {s['neg']}.
- Rien n'est publié, activé ni mis en production sans une personne autorisée ; aucun score, classement ou citation par une IA n'est promis.
- Les parties non prises en charge par Éclair 2.0 sont explicitement signalées comme **non livrables en production**.

**Statut de maturité de ce skill :** `{MATURITY[m]}`. Voir `references/acceptance.md` pour les cas d'essai reproductibles.
"""


def native_contract(s):
    return f"""# Application du contrat natif au skill {s['name']}

Ce skill utilise exclusivement ce que livre Éclair CMS 2.0.x : les fonctions du noyau, le contrat de thème et le contrat `eclair-extension/1`. Référence officielle : https://github.com/Jacckisback/eclair-cms/blob/main/docs/EXTENSION-CONTRACT.md

## Position de ce skill

{CONTRACT[s['mat']]}

## Garde-fou pratique

Sur un vrai checkout, relire `eclair/index.php`, exécuter `php tools/validate.php` sur tout paquet produit et `php tests/run.php`. Si la demande dépasse les fonctions natives, les routes GET publiques, les pages d'administration protégées, les blocs, les réglages et `Store`, produire une demande d'évolution distincte ; **ne jamais simuler sa disponibilité**.
"""


def family_contract(title, limitation):
    return f"""# Contrat de la famille {title}

Cible : **Éclair CMS 2.0.x**, extension **`eclair-extension/1`**, identifiants et version découverts avant toute modification.

**Capacités natives à privilégier :** fonctions déjà intégrées au noyau (voir `core-map.md`), thèmes dans `site/themes/`, extensions dans `site/extensions/`, données `Store` sous `$ctx['data']`, routes GET publiques et GET/POST d'administration protégées, tâches planifiées, migrations, validation `tools/validate.php`, suite PHP, mesures.

**Limitations de production :** {limitation}

**Politique agent :** utiliser d'abord le natif, générer le minimum de code, garder le noyau intact, refuser de présenter une maquette comme une fonctionnalité en service ; demander une évolution du noyau quand elle est nécessaire. Les changements à forte portée (paiement, contenu privé, e-mails, données personnelles ou de santé) exigent des tests réels et une validation humaine avant activation.

**Points de sécurité :** contrôler chaque objet et chaque écriture ; protéger formulaires, secrets, signatures et données personnelles ; vérifier erreurs et retour arrière ; ne garder en cache public que du HTML sans donnée d'utilisateur. Ne pas confondre `eclair-extension/1` et les API expérimentales antérieures.
"""


def acceptance(s):
    return f"""# Plan de validation — {s['title']}

## Modèle de données
{s['model']}.

## Mise en œuvre attendue
{s['procedure']}.

## Tests à prévoir
1. Nominal : {s['pos']}.
2. Contrôle de refus : {s['neg']}.
3. Invariant : {s['invariant']}.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
"""


def outputs():
    cat = json.loads((ROOT / 'catalog.json').read_text(encoding='utf-8'))
    generated = specs()
    gen_names = {s['name'] for rows in generated.values() for s in rows}
    # Keep hand-written skills, drop previously generated entries, then append.
    kept = [s for s in cat['skills'] if s['name'] not in gen_names]
    if len({s['name'] for s in kept}) + len(gen_names) != len(kept) + sum(len(r) for r in generated.values()):
        raise SystemExit('Duplicate skill names between specs')
    groups = dict(cat['groups'])
    for key, (title, desc, _lim) in NEW_GROUPS.items():
        groups.setdefault(key, {})
        groups[key].update(title=title, description=desc)
    skills = []
    for key in ORDER:
        skills += [s for s in kept if s['category'] == key]
        skills += [{'name': s['name'], 'category': key, 'maturity': MATURITY[s['mat']], 'kind': 'agent-skill'}
                   for s in generated.get(key, [])]
    if len(skills) != len(kept) + len(gen_names):
        raise SystemExit('A skill belongs to a family missing from ORDER')
    for key in ORDER:
        groups[key]['count'] = sum(1 for s in skills if s['category'] == key)
    cat['groups'] = {k: groups[k] for k in ORDER}
    cat['skills'] = skills
    cat['catalog_version'] = VERSION
    cat['generated_for'] = 'wordpress-alternative-catalogue'
    cat['status'] = 'workflow-library-core-builtin-and-native-usable-transactional-modules-design-only'
    cat['notes'] = [
        f'All {len(skills)} entries are agent skills (guides), not {len(skills)} working PHP plugins.',
        'Maturity core-builtin-configuration-workflow: the feature already exists in the Éclair core; the skill configures and checks it.',
        'Extensions expose public GET routes only on Éclair 2.0; public POST (PR #19) is a draft, not merged.',
        'Catalogue demo is a read-only example, no commerce transactions.',
    ]
    files = {'catalog.json': json.dumps(cat, indent=2, ensure_ascii=False) + '\n'}
    for s in skills:
        files[f"skills/{s['name']}/references/core-map.md"] = CORE_MAP
    for key, rows in generated.items():
        g = cat['groups'][key]
        limitation = NEW_GROUPS[key][2] if key in NEW_GROUPS else None
        for s in rows:
            base = f"skills/{s['name']}"
            files[f'{base}/SKILL.md'] = skill_md(s, g['title'])
            files[f'{base}/references/native-contract.md'] = native_contract(s)
            files[f'{base}/references/acceptance.md'] = acceptance(s)
            if limitation is None:
                # Existing family: reuse its hand-written family contract.
                ref = next(k['name'] for k in kept if k['category'] == key)
                files[f'{base}/references/family-contract.md'] = (ROOT / 'skills' / ref / 'references/family-contract.md').read_text(encoding='utf-8')
            else:
                files[f'{base}/references/family-contract.md'] = family_contract(g['title'], limitation)
    return files


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true')
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
            print('FAIL: regenerate with python3 scripts/build_skills.py:\n- ' + '\n- '.join(stale[:20]))
            return 1
        print(f'PASS: {len(files)} generated skill files are up to date')
        return 0
    print(f'WROTE {len(files)} files')
    return 0


if __name__ == '__main__':
    sys.exit(main())
