---
name: eclair-structured-data
description: "Add or check schema.org data consistent with the visible content. Use on Éclair CMS 2.x when the user wants to: ajouter ou vérifier schema.org cohérent avec le contenu. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Données structurées — Éclair CMS 2.x

## Déclencheur et résultat attendu
Utiliser ce skill pour **ajouter ou vérifier schema.org cohérent avec le contenu**. Cette fonction est **en partie bloquée par le contrat du noyau** : le skill livre ce qui est natif et documente l'écart. Ce skill est un **workflow d'agent**, pas une extension PHP fonctionnelle ni une garantie de conformité.

**Équivalent WordPress :** Schema Pro, Rank Math Schema. Famille : SEO, GEO et migration.

## Diagnostic obligatoire avant modification
1. Lire `references/core-map.md` (ce que le noyau fait déjà) et `references/native-contract.md` ; vérifier la version réelle du CMS et les capacités dans `GET /<admin>/api/capabilities` (si l'accès est autorisé).
2. Lire `references/family-contract.md` et `references/acceptance.md`. Ne jamais copier l'ancien système de packs v0.x ni du code PHP de WordPress dans Éclair 2.
3. Identifier le modèle de données : **WebPage, Article, Product, FAQ pertinente, Organization, BreadcrumbList**. Documenter ce qui est public, ce qui est privé et d'où vient chaque donnée.

## Procédure spécifique
4. **Parcours :** Inspecter JSON-LD natif avant d’ajouter un type; éviter duplication; aligner chaque champ avec les données visibles et les consignes des moteurs. Décrire les états et les erreurs avant d'écrire du code.
5. **Emplacements :** code propre au site dans `site/extensions/<id>/`, apparence dans `site/themes/<id>/`, données sous `$ctx['data']`, contenus et réglages par l'administration ou le MCP. Ne jamais éditer `app/`, `assets/`, `index.php` ni l'updater.
6. **Contrat actuel :** Les SEO/GEO de base sont natifs. Les extensions ne disposent pas encore d’une API universelle pour injecter le JSON-LD; documenter l’écart de contrat plutôt que bricoler le HTML ou des scripts.
7. **Invariant de sécurité :** Éclair v2 n’expose pas encore toutes les contributions JSON-LD aux extensions; proposer RFC plutôt qu’injection opaque. Vérifier aussi les droits côté serveur, l'échappement avec `e()`, la validation des données et l'absence de secret ou de donnée personnelle dans le HTML public ou un cache partagé.
8. **Preuves :** écrire le test positif « Tester JSON valide, canonical, identifiants et contenu affiché » et le test de refus « Aucun prix/avis/product inventé ou absent de la page ne figure en JSON-LD ». Mesurer les régressions de SEO et de performance, documenter le retour arrière.
9. **Validation native :** `php tools/validate.php <dossier> --json`, `php tests/run.php` et `php tools/measure.php --check` sur un checkout officiel pour tout paquet produit. Pour une partie non prise en charge par le noyau, fournir une note d'écart et un test bloquant, jamais une réussite fictive.

## Livrables obligatoires
- Mini-spécification : objectif, utilisateurs, parcours, états, données, mesures.
- Matrice d'autorisations et de cache : route, méthode, session, visibilité, indexation.
- Paquet ou réglages pour la partie native, et note d'écart précise pour la partie bloquée.
- Tests des cas positifs et des refus, procédure de désactivation qui conserve les données, note de compatibilité.

## Critères d'acceptation
- Tester JSON valide, canonical, identifiants et contenu affiché.
- Aucun prix/avis/product inventé ou absent de la page ne figure en JSON-LD.
- Rien n'est publié, activé ni mis en production sans une personne autorisée ; aucun score, classement ou citation par une IA n'est promis.
- Les parties non prises en charge par Éclair 2.0 sont explicitement signalées comme **non livrables en production**.

**Statut de maturité de ce skill :** `partly-blocked-by-core-contract`. Voir `references/acceptance.md` pour les cas d'essai reproductibles.
