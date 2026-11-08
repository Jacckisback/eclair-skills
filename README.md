# Éclair Skills — catalogue complet v2.0.0

**57 Agent Skills opérationnels au niveau des workflows** (8 fondamentaux + 49 métiers) pour créer ou améliorer des sites Éclair CMS 2.0.x avec Codex, ChatGPT et Claude. **Ils ne sont pas 57 extensions PHP fonctionnelles.** Ils guident l'agent dans le choix du bon contrat, les livrables, l'écriture du code autorisé et les tests de non-régression.

## Groupes

| Famille | Nombre | Portée |
|---|---:|---|
| Fondations | 8 | Contrat natif v2, tests et sécurité |
| Commerce Pro | 10 | Boutique transactionnelle et paiement, conception avant déploiement |
| LMS | 7 | Cours, inscriptions, progression, certifications |
| Forum et communauté | 6 | Discussions, modération, profils et notifications |
| Applications métiers | 8 | Réservations, abonnements, annuaires et outils métiers |
| Design et UX | 7 | Thèmes, blocs, accessibilité et rapidité |
| SEO, GEO et migration | 5 | Indexabilité, données structurées et WordPress |
| Intégrations et automatisations | 6 | API, webhooks, emails, IA, suivi |

## Installation dans un projet agent

```bash
python3 scripts/validate_skills.py
python3 scripts/install_skills.py --list
python3 scripts/install_skills.py --project /chemin/mon-site --category commerce
python3 scripts/install_skills.py --project /chemin/mon-site --category lms
python3 scripts/install_skills.py --project /chemin/mon-site --skill eclair-wordpress-migration
python3 scripts/install_skills.py --project /chemin/mon-site --all
```

Sans option de filtrage, tous les skills sont sélectionnés. L'installateur refuse d'écraser un skill existant (utiliser `--force` explicitement après revue). Un skill est autonome : `SKILL.md` + `references/` locales.

## Démo PHP native Éclair v2

`examples/extensions/catalogue-demo` : vitrine **lecture seule**, route GET `/catalogue-demo`, sans clients, paiement ni commande. Pour le packager en ZIP : ne mettre que `extension.json` et `extension.php` à la racine du dossier. Sur un clone du vrai CMS, tester :

```bash
php tools/validate.php /chemin/eclair-skills-complete-v2.0.0/examples/extensions/catalogue-demo --json
php tests/run.php
php tools/measure.php --check
```

Les résultats du validateur officiel ne sont pas fournis ici : l'environnement local ne dispose pas du checkout officiel. Les tests Python et PHP propres au kit sont distincts.

## État de la fondation et des modules

- Huit skills de base : prêts à guider un agent pour l'architecture v2.
- [PR #19](https://github.com/Jacckisback/eclair-cms/pull/19) : route POST publique expérimentale; CI du dernier commit réussie au 8/11/2026, **en brouillon, non fusionnée**. Pas une autorisation de déploiement.
- `examples/extensions/member-directory` : prototype indépendant, non qualifié; inscription et récupération désactivées par défaut.
- Catalogue/LMS/Forum/commerce/CRM etc. : guides de construction, **pas des applications prêtes à l'emploi**.
- `docs/CAPABILITY_MATRIX.md` et `docs/ROADMAP_57.md` distinguent contrats natifs, lacunes et étapes d'implémentation.

## Tests du kit

```bash
python3 -m unittest discover -s tests -p 'test_*.py' -v
python3 scripts/verify_sample.py
php -l examples/extensions/catalogue-demo/extension.php
php tests/member-directory.php
php tests/member-public.php
php tests/member-enroll.php
```

**Important :** les tests de Member Directory sont isolés et ne valent pas tests HTTP/SMTP, ni audit production. Ne pas remplacer le moteur d'extensions v2 par celui des anciennes archives v0.x.

## Contrôles de publication

```bash
python3 scripts/validate_skills.py
python3 scripts/check_release.py          # SHA-256, licence, 57 skills / 8 familles
python3 scripts/verify_member_directory.py
```

`SHA256SUMS.json` couvre tous les fichiers du dépôt sauf lui-même ; après une modification volontaire : `python3 scripts/check_release.py --write`. La CI GitHub (`.github/workflows/validate.yml`) exécute ces contrôles et les tests ci-dessus ; **elle ne prouve pas la sécurité en production** des modules expérimentaux.

Catalogue détaillé : [docs/CATALOGUE_COMPLET.md](docs/CATALOGUE_COMPLET.md) · Contribuer : [CONTRIBUTING.md](CONTRIBUTING.md) · Sécurité : [SECURITY.md](SECURITY.md)

## Licence

GNU Affero General Public License v3.0 only (`AGPL-3.0-only`), comme Éclair CMS. Texte intégral officiel : [LICENSE](LICENSE). Les notices de copyright présentes dans les fichiers sont conservées.

---

## English

**Éclair Skills v2.0.0 — 57 Agent Skills for Éclair CMS 2.0.x** (native extension contract `eclair-extension/1`), usable with Claude Code, Codex, ChatGPT and other agents that read `SKILL.md` folders.

- **57 skills ≠ 57 PHP extensions.** Each skill is a self-contained workflow guide (`SKILL.md` + local `references/`) that helps an agent choose the right contract, write allowed code and test it.
- **Eight families:** Foundations (8), Commerce Pro (10), LMS (7), Forum & community (6), Business apps (8), Design & UX (7), SEO, GEO & migration (5), Integrations & automation (6). Full list: [docs/CATALOGUE_COMPLET.md](docs/CATALOGUE_COMPLET.md).
- **Install** into a project: `python3 scripts/install_skills.py --project /path/to/site --category commerce` (or `--skill <name>`, `--all`). The installer never overwrites an existing skill unless `--force` is given after review.
- **Examples:** `examples/extensions/catalogue-demo` is a read-only GET demo (no customers, payment or orders). `examples/extensions/member-directory` and `core-patch/` are **experimental prototypes, not production-ready**; the public POST route depends on the unmerged draft [eclair-cms PR #19](https://github.com/Jacckisback/eclair-cms/pull/19).
- **No guarantees:** Lighthouse scores, Google rankings and AI citations must be measured; nothing here guarantees them.
- **Licence:** AGPL-3.0-only — see [LICENSE](LICENSE).
