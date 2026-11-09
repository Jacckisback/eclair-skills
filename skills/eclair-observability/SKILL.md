---
name: eclair-observability
description: "Monitor health, costs and incidents of modules, with alerts. Use on Éclair CMS 2.x when the user wants to: surveiller santé, coûts et incidents des modules. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Observabilité et alertes — Éclair CMS 2.x

## Déclencheur et résultat attendu
Utiliser ce skill pour **surveiller santé, coûts et incidents des modules**. Il produit une architecture vérifiable, les changements de site autorisés, des tests positifs et négatifs et une note sur les dépendances au noyau. Ce skill est un **workflow d'agent**, pas une extension PHP fonctionnelle ni une garantie de conformité.

## Diagnostic obligatoire avant modification
1. Lire `references/core-map.md` et `references/native-contract.md` ; vérifier version réelle du CMS, manifeste `eclair-extension/1` et les capacités disponibles dans `GET /<admin>/api/capabilities` (si accès autorisé).
2. Lire `references/family-contract.md` et `references/acceptance.md` pour ce domaine. Ne jamais copier l'ancien système de packs v0.x dans Éclair 2.
3. Identifier le modèle de données : **Logs structurés, erreurs, corrélations, métriques, traces, rétention**. Documenter chaque champ privé/public et la provenance des données.

## Procédure spécifique
4. **Parcours métier :** Définir alertes utiles, anonymiser données, surveiller tâches et cache, distinguer incident site et module, fournir runbook. Dessiner les états et les erreurs avant d'écrire du code.
5. **Emplacements :** conserver tout code propriétaire au site dans `site/extensions/<id>/`, l'apparence dans `site/themes/<id>/` ; enregistrer les données dans le préfixe `Store` fourni par `$ctx['data']`. Ne jamais éditer `app/`, `assets/`, `index.php` ou l'updater dans le cadre de ce skill.
6. **Contrat actuel :** Les tâches natives existent (minimum 3 600 secondes). Les webhooks entrants et interactions membres requièrent des routes POST qualifiées, une validation de signature et, pour les effets métiers, une outbox idempotente.
7. **Invariant de sécurité :** Aucun mot de passe, jeton, paiement ou PII brute dans les logs; pas de télémétrie cachée. Vérifier droits serveur sur chaque objet, échappement avec `e()`, validation des données, absence de secret et de PII dans le HTML public ou un cache partagé.
8. **Preuves :** écrire test positif « Tester hausse erreurs 5xx, retard des tâches et disque plein » et test de rejet « Un module désactivé ne continue pas à envoyer de données ni à exécuter de tâches ». Mesurer les régressions SEO/performance, documenter rollback et responsabilité des données.
9. **Validation native :** `php tools/validate.php <dossier> --json`, `php tests/run.php` et `php tools/measure.php --check` sur le checkout officiel (si extension installable). Pour une fonctionnalité non supportée par le noyau actuel, fournir une RFC et un test bloquant, pas une assertion de réussite fictive.

## Livrables obligatoires
- Mini-spécification : objectifs, utilisateurs, parcours, états, données, métriques.
- Matrice d'autorisations et de cache : route, méthode, session, visibilité, indexation.
- Paquet `extension.json`/`extension.php` seulement si le contrat natif supporte réellement les opérations ; sinon plan d'extension ou maquette GET sûre.
- Tests démontrant les cas positifs et les refus, procédure de désactivation conservant les données et note de compatibilité.

## Critères d'acceptation
- Tester hausse erreurs 5xx, retard des tâches et disque plein.
- Un module désactivé ne continue pas à envoyer de données ni à exécuter de tâches.
- Les parcours non pris en charge par Éclair v2 sont explicitement signalés comme **non livrables en production**.

**Statut de maturité de ce skill :** `design-workflow-requires-verified-core-capabilities`. Voir `references/acceptance.md` pour les cas d'essai reproductibles.
