---
name: eclair-blog-posts
description: "Publish and organise blog posts with the native block editor. Use on Éclair CMS 2.x when the user wants to: publier et organiser des articles de blog avec l'éditeur de blocs natif. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Articles de blog — Éclair CMS 2.x

## Déclencheur et résultat attendu
Utiliser ce skill pour **publier et organiser des articles de blog avec l'éditeur de blocs natif**. Cette fonction est **déjà intégrée au noyau Éclair 2.0** : le skill guide sa configuration et sa vérification, sans écrire d'extension. Ce skill est un **workflow d'agent**, pas une extension PHP fonctionnelle ni une garantie de conformité.

**Équivalent WordPress :** Articles natifs de WordPress. Famille : Contenu et édition.

## Diagnostic obligatoire avant modification
1. Lire `references/core-map.md` (ce que le noyau fait déjà) et `references/native-contract.md` ; vérifier la version réelle du CMS et les capacités dans `GET /<admin>/api/capabilities` (si l'accès est autorisé).
2. Lire `references/family-contract.md` et `references/acceptance.md`. Ne jamais copier l'ancien système de packs v0.x ni du code PHP de WordPress dans Éclair 2.
3. Identifier le modèle de données : **Article, extrait, image principale, catégorie, auteur, date, statut brouillon ou publié**. Documenter ce qui est public, ce qui est privé et d'où vient chaque donnée.

## Procédure spécifique
4. **Parcours :** Créer les articles en brouillon par l'administration ou le connecteur MCP, vérifier titre, extrait, image et catégorie, puis laisser une personne publier. Décrire les états et les erreurs avant d'écrire du code.
5. **Emplacements :** code propre au site dans `site/extensions/<id>/`, apparence dans `site/themes/<id>/`, données sous `$ctx['data']`, contenus et réglages par l'administration ou le MCP. Ne jamais éditer `app/`, `assets/`, `index.php` ni l'updater.
6. **Contrat actuel :** La fonction existe dans le noyau : la régler par l'administration ou, en brouillon, par le connecteur MCP. Ne pas la dupliquer dans une extension et ne jamais modifier le noyau pour l'adapter ; si un besoin dépasse ce que le noyau offre, le signaler comme un écart.
7. **Invariant de sécurité :** Ne jamais publier ni supprimer un contenu à la place de la personne autorisée. Vérifier aussi les droits côté serveur, l'échappement avec `e()`, la validation des données et l'absence de secret ou de donnée personnelle dans le HTML public ou un cache partagé.
8. **Preuves :** écrire le test positif « Créer un brouillon complet, le faire publier, puis vérifier son rendu, le flux RSS et le sitemap » et le test de refus « Un brouillon n'apparaît ni sur le site public, ni dans le sitemap, ni dans le flux ». Mesurer les régressions de SEO et de performance, documenter le retour arrière.
9. **Validation native :** `php tools/validate.php <dossier> --json`, `php tests/run.php` et `php tools/measure.php --check` sur un checkout officiel pour tout paquet produit. Pour une partie non prise en charge par le noyau, fournir une note d'écart et un test bloquant, jamais une réussite fictive.

## Livrables obligatoires
- Mini-spécification : objectif, utilisateurs, parcours, états, données, mesures.
- Matrice d'autorisations et de cache : route, méthode, session, visibilité, indexation.
- Réglages et contenus préparés par l'administration ou en brouillon par le MCP ; **aucune extension** tant que le natif suffit.
- Tests des cas positifs et des refus, procédure de désactivation qui conserve les données, note de compatibilité.

## Critères d'acceptation
- Créer un brouillon complet, le faire publier, puis vérifier son rendu, le flux RSS et le sitemap.
- Un brouillon n'apparaît ni sur le site public, ni dans le sitemap, ni dans le flux.
- Rien n'est publié, activé ni mis en production sans une personne autorisée ; aucun score, classement ou citation par une IA n'est promis.
- Les parties non prises en charge par Éclair 2.0 sont explicitement signalées comme **non livrables en production**.

**Statut de maturité de ce skill :** `core-builtin-configuration-workflow`. Voir `references/acceptance.md` pour les cas d'essai reproductibles.
