---
name: eclair-custom-content-types
description: "Model business content (projects, listings, events) without core custom post types. Use on Éclair CMS 2.x when the user wants to: modéliser des contenus métier (réalisations, biens, événements) sans type de contenu personnalisé dans le noyau. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Types de contenu personnalisés — Éclair CMS 2.x

## Déclencheur et résultat attendu
Utiliser ce skill pour **modéliser des contenus métier (réalisations, biens, événements) sans type de contenu personnalisé dans le noyau**. Cette fonction est **en partie bloquée par le contrat du noyau** : le skill livre ce qui est natif et documente l'écart. Ce skill est un **workflow d'agent**, pas une extension PHP fonctionnelle ni une garantie de conformité.

**Équivalent WordPress :** Custom Post Types (CPT UI, ACF). Famille : Contenu et édition.

## Diagnostic obligatoire avant modification
1. Lire `references/core-map.md` (ce que le noyau fait déjà) et `references/native-contract.md` ; vérifier la version réelle du CMS et les capacités dans `GET /<admin>/api/capabilities` (si l'accès est autorisé).
2. Lire `references/family-contract.md` et `references/acceptance.md`. Ne jamais copier l'ancien système de packs v0.x ni du code PHP de WordPress dans Éclair 2.
3. Identifier le modèle de données : **Fiche métier, champs, liste, adresse, statut**. Documenter ce qui est public, ce qui est privé et d'où vient chaque donnée.

## Procédure spécifique
4. **Parcours :** Choisir entre pages avec blocs dédiés et extension avec stockage propre et routes GET, fixer les adresses, prévoir liste et fiche. Décrire les états et les erreurs avant d'écrire du code.
5. **Emplacements :** code propre au site dans `site/extensions/<id>/`, apparence dans `site/themes/<id>/`, données sous `$ctx['data']`, contenus et réglages par l'administration ou le MCP. Ne jamais éditer `app/`, `assets/`, `index.php` ni l'updater.
6. **Contrat actuel :** Une partie dépend d'un point d'accroche absent du contrat 2.0 (types de contenu, contribution SEO ou JSON-LD, politique de contenu par fonction, filtre de rendu). Livrer la partie native et documenter précisément l'écart, sans contournement.
7. **Invariant de sécurité :** Ne jamais écrire dans les fichiers de contenus du noyau depuis une extension. Vérifier aussi les droits côté serveur, l'échappement avec `e()`, la validation des données et l'absence de secret ou de donnée personnelle dans le HTML public ou un cache partagé.
8. **Preuves :** écrire le test positif « Créer un type de fiche par extension, avec liste et détail en GET, puis valider le paquet » et le test de refus « Une fiche non publiée n'est servie ni en liste ni par son adresse directe ». Mesurer les régressions de SEO et de performance, documenter le retour arrière.
9. **Validation native :** `php tools/validate.php <dossier> --json`, `php tests/run.php` et `php tools/measure.php --check` sur un checkout officiel pour tout paquet produit. Pour une partie non prise en charge par le noyau, fournir une note d'écart et un test bloquant, jamais une réussite fictive.

## Livrables obligatoires
- Mini-spécification : objectif, utilisateurs, parcours, états, données, mesures.
- Matrice d'autorisations et de cache : route, méthode, session, visibilité, indexation.
- Paquet ou réglages pour la partie native, et note d'écart précise pour la partie bloquée.
- Tests des cas positifs et des refus, procédure de désactivation qui conserve les données, note de compatibilité.

## Critères d'acceptation
- Créer un type de fiche par extension, avec liste et détail en GET, puis valider le paquet.
- Une fiche non publiée n'est servie ni en liste ni par son adresse directe.
- Rien n'est publié, activé ni mis en production sans une personne autorisée ; aucun score, classement ou citation par une IA n'est promis.
- Les parties non prises en charge par Éclair 2.0 sont explicitement signalées comme **non livrables en production**.

**Statut de maturité de ce skill :** `partly-blocked-by-core-contract`. Voir `references/acceptance.md` pour les cas d'essai reproductibles.
