---
name: eclair-notifications
description: "Use when a user wants to informer sans spam ni fuite de données on Éclair CMS 2.x; design a notifications de communauté workflow with native extension compatibility, security and acceptance gates."
---

# Notifications de communauté — Éclair CMS 2.x

## Déclencheur et résultat attendu
Utiliser ce skill pour **informer sans spam ni fuite de données**. Il produit une architecture vérifiable, les changements de site autorisés, des tests positifs et négatifs et une note sur les dépendances au noyau. Ce skill est un **workflow d'agent**, pas une extension PHP fonctionnelle ni une garantie de conformité.

## Diagnostic obligatoire avant modification
1. Lire `references/core-map.md` et `references/native-contract.md` ; vérifier version réelle du CMS, manifeste `eclair-extension/1` et les capacités disponibles dans `GET /<admin>/api/capabilities` (si accès autorisé).
2. Lire `references/family-contract.md` et `references/acceptance.md` pour ce domaine. Ne jamais copier l'ancien système de packs v0.x dans Éclair 2.
3. Identifier le modèle de données : **Abonnement, mention, notification, canal, préférence, statut**. Documenter chaque champ privé/public et la provenance des données.

## Procédure spécifique
4. **Parcours métier :** Émettre événements après écriture validée, filtrer par droits au moment de la lecture et de l’envoi, appliquer désabonnement. Dessiner les états et les erreurs avant d'écrire du code.
5. **Emplacements :** conserver tout code propriétaire au site dans `site/extensions/<id>/`, l'apparence dans `site/themes/<id>/` ; enregistrer les données dans le préfixe `Store` fourni par `$ctx['data']`. Ne jamais éditer `app/`, `assets/`, `index.php` ou l'updater dans le cadre de ce skill.
6. **Contrat actuel :** Les catégories et listes publiques peuvent être GET; publications, signalements, profils privés et modération exigent une identité et des routes d’écriture sûres, anti-spam et stockage adapté.
7. **Invariant de sécurité :** Ne jamais révéler contenu de catégories privées dans email push ou digest. Vérifier droits serveur sur chaque objet, échappement avec `e()`, validation des données, absence de secret et de PII dans le HTML public ou un cache partagé.
8. **Preuves :** écrire test positif « Tester notifications répétées, désabonnement et retrait de permission » et test de rejet « Après révocation d’accès, aucune nouvelle notification ne contient un extrait privé ». Mesurer les régressions SEO/performance, documenter rollback et responsabilité des données.
9. **Validation native :** `php tools/validate.php <dossier> --json`, `php tests/run.php` et `php tools/measure.php --check` sur le checkout officiel (si extension installable). Pour une fonctionnalité non supportée par le noyau actuel, fournir une RFC et un test bloquant, pas une assertion de réussite fictive.

## Livrables obligatoires
- Mini-spécification : objectifs, utilisateurs, parcours, états, données, métriques.
- Matrice d'autorisations et de cache : route, méthode, session, visibilité, indexation.
- Paquet `extension.json`/`extension.php` seulement si le contrat natif supporte réellement les opérations ; sinon plan d'extension ou maquette GET sûre.
- Tests démontrant les cas positifs et les refus, procédure de désactivation conservant les données et note de compatibilité.

## Critères d'acceptation
- Tester notifications répétées, désabonnement et retrait de permission.
- Après révocation d’accès, aucune nouvelle notification ne contient un extrait privé.
- Les parcours non pris en charge par Éclair v2 sont explicitement signalés comme **non livrables en production**.

**Statut de maturité de ce skill :** `design-workflow-requires-verified-core-capabilities`. Voir `references/acceptance.md` pour les cas d'essai reproductibles.
