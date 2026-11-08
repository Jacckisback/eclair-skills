---
name: eclair-orders-payments
description: "Use when a user wants to implémenter les états de commande et des prestataires psp on Éclair CMS 2.x; design a commandes et paiements workflow with native extension compatibility, security and acceptance gates."
---

# Commandes et paiements — Éclair CMS 2.x

## Déclencheur et résultat attendu
Utiliser ce skill pour **implémenter les états de commande et des prestataires psp**. Il produit une architecture vérifiable, les changements de site autorisés, des tests positifs et négatifs et une note sur les dépendances au noyau. Ce skill est un **workflow d'agent**, pas une extension PHP fonctionnelle ni une garantie de conformité.

## Diagnostic obligatoire avant modification
1. Lire `references/core-map.md` et `references/native-contract.md` ; vérifier version réelle du CMS, manifeste `eclair-extension/1` et les capacités disponibles dans `GET /<admin>/api/capabilities` (si accès autorisé).
2. Lire `references/family-contract.md` et `references/acceptance.md` pour ce domaine. Ne jamais copier l'ancien système de packs v0.x dans Éclair 2.
3. Identifier le modèle de données : **Commande, tentative de paiement, identifiant fournisseur, preuve webhook, idempotency key, remboursement**. Documenter chaque champ privé/public et la provenance des données.

## Procédure spécifique
4. **Parcours métier :** Détailler les transitions autorisées; stocker la preuve de la notification et son horodatage; traiter webhook durablement; prévoir reconciliation et remboursement partiel. Dessiner les états et les erreurs avant d'écrire du code.
5. **Emplacements :** conserver tout code propriétaire au site dans `site/extensions/<id>/`, l'apparence dans `site/themes/<id>/` ; enregistrer les données dans le préfixe `Store` fourni par `$ctx['data']`. Ne jamais éditer `app/`, `assets/`, `index.php` ou l'updater dans le cadre de ce skill.
6. **Contrat actuel :** Panier, commandes et paiements ont besoin de POST publics, d’un stockage transactionnel fiable, de webhooks authentifiés et d’idempotence; Éclair 2.0 officiel ne fournit pas tout cela. La PR #19 est encore un brouillon : ne jamais utiliser une route POST non fusionnée comme preuve de compatibilité.
7. **Invariant de sécurité :** Ne jamais stocker données de carte bancaire brutes; checkout hébergé chez le prestataire et signature des webhooks vérifiée. Vérifier droits serveur sur chaque objet, échappement avec `e()`, validation des données, absence de secret et de PII dans le HTML public ou un cache partagé.
8. **Preuves :** écrire test positif « Tester webhook inversé, hors ordre, réémis et paiement refusé » et test de rejet « Un webhook sans signature valide ne modifie ni commande ni accès LMS ». Mesurer les régressions SEO/performance, documenter rollback et responsabilité des données.
9. **Validation native :** `php tools/validate.php <dossier> --json`, `php tests/run.php` et `php tools/measure.php --check` sur le checkout officiel (si extension installable). Pour une fonctionnalité non supportée par le noyau actuel, fournir une RFC et un test bloquant, pas une assertion de réussite fictive.

## Livrables obligatoires
- Mini-spécification : objectifs, utilisateurs, parcours, états, données, métriques.
- Matrice d'autorisations et de cache : route, méthode, session, visibilité, indexation.
- Paquet `extension.json`/`extension.php` seulement si le contrat natif supporte réellement les opérations ; sinon plan d'extension ou maquette GET sûre.
- Tests démontrant les cas positifs et les refus, procédure de désactivation conservant les données et note de compatibilité.

## Critères d'acceptation
- Tester webhook inversé, hors ordre, réémis et paiement refusé.
- Un webhook sans signature valide ne modifie ni commande ni accès LMS.
- Les parcours non pris en charge par Éclair v2 sont explicitement signalés comme **non livrables en production**.

**Statut de maturité de ce skill :** `design-workflow-requires-verified-core-capabilities`. Voir `references/acceptance.md` pour les cas d'essai reproductibles.
