---
name: eclair-structured-data
description: "Add or check schema.org data consistent with the visible content. Use on Éclair CMS 2.x when the user wants to: ajouter ou vérifier schema.org cohérent avec le contenu. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Données structurées — Éclair CMS 2.x

## Déclencheur et résultat attendu
Utiliser ce skill pour **ajouter ou vérifier schema.org cohérent avec le contenu**. Il produit une architecture vérifiable, les changements de site autorisés, des tests positifs et négatifs et une note sur les dépendances au noyau. Ce skill est un **workflow d'agent**, pas une extension PHP fonctionnelle ni une garantie de conformité.

## Diagnostic obligatoire avant modification
1. Lire `references/core-map.md` et `references/native-contract.md` ; vérifier version réelle du CMS, manifeste `eclair-extension/1` et les capacités disponibles dans `GET /<admin>/api/capabilities` (si accès autorisé).
2. Lire `references/family-contract.md` et `references/acceptance.md` pour ce domaine. Ne jamais copier l'ancien système de packs v0.x dans Éclair 2.
3. Identifier le modèle de données : **WebPage, Article, Product, FAQ pertinente, Organization, BreadcrumbList**. Documenter chaque champ privé/public et la provenance des données.

## Procédure spécifique
4. **Parcours métier :** Inspecter JSON-LD natif avant d’ajouter un type; éviter duplication; aligner chaque champ avec les données visibles et les consignes des moteurs. Dessiner les états et les erreurs avant d'écrire du code.
5. **Emplacements :** conserver tout code propriétaire au site dans `site/extensions/<id>/`, l'apparence dans `site/themes/<id>/` ; enregistrer les données dans le préfixe `Store` fourni par `$ctx['data']`. Ne jamais éditer `app/`, `assets/`, `index.php` ou l'updater dans le cadre de ce skill.
6. **Contrat actuel :** Les SEO/GEO de base sont natifs. Les extensions ne disposent pas encore d’une API universelle pour injecter le JSON-LD; documenter l’écart de contrat plutôt que bricoler le HTML ou des scripts.
7. **Invariant de sécurité :** Éclair v2 n’expose pas encore toutes les contributions JSON-LD aux extensions; proposer RFC plutôt qu’injection opaque. Vérifier droits serveur sur chaque objet, échappement avec `e()`, validation des données, absence de secret et de PII dans le HTML public ou un cache partagé.
8. **Preuves :** écrire test positif « Tester JSON valide, canonical, identifiants et contenu affiché » et test de rejet « Aucun prix/avis/product inventé ou absent de la page ne figure en JSON-LD ». Mesurer les régressions SEO/performance, documenter rollback et responsabilité des données.
9. **Validation native :** `php tools/validate.php <dossier> --json`, `php tests/run.php` et `php tools/measure.php --check` sur le checkout officiel (si extension installable). Pour une fonctionnalité non supportée par le noyau actuel, fournir une RFC et un test bloquant, pas une assertion de réussite fictive.

## Livrables obligatoires
- Mini-spécification : objectifs, utilisateurs, parcours, états, données, métriques.
- Matrice d'autorisations et de cache : route, méthode, session, visibilité, indexation.
- Paquet `extension.json`/`extension.php` seulement si le contrat natif supporte réellement les opérations ; sinon plan d'extension ou maquette GET sûre.
- Tests démontrant les cas positifs et les refus, procédure de désactivation conservant les données et note de compatibilité.

## Critères d'acceptation
- Tester JSON valide, canonical, identifiants et contenu affiché.
- Aucun prix/avis/product inventé ou absent de la page ne figure en JSON-LD.
- Les parcours non pris en charge par Éclair v2 sont explicitement signalés comme **non livrables en production**.

**Statut de maturité de ce skill :** `partly-blocked-by-core-contract`. Voir `references/acceptance.md` pour les cas d'essai reproductibles.
