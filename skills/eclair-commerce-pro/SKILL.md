---
name: eclair-commerce-pro
description: "Design a complete shop, from catalogue to delivered order (entry point of the family). Use on Éclair CMS 2.x when the user wants to: concevoir une boutique complète, du catalogue à la commande livrée. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Architecture Commerce Pro — Éclair CMS 2.x

## Déclencheur et résultat attendu
Utiliser ce skill pour **concevoir une boutique complète, du catalogue à la commande livrée**. Il produit une architecture vérifiable, les changements de site autorisés, des tests positifs et négatifs et une note sur les dépendances au noyau. Ce skill est un **workflow d'agent**, pas une extension PHP fonctionnelle ni une garantie de conformité.

## Diagnostic obligatoire avant modification
1. Lire `references/core-map.md` et `references/native-contract.md` ; vérifier version réelle du CMS, manifeste `eclair-extension/1` et les capacités disponibles dans `GET /<admin>/api/capabilities` (si accès autorisé).
2. Lire `references/family-contract.md` et `references/acceptance.md` pour ce domaine. Ne jamais copier l'ancien système de packs v0.x dans Éclair 2.
3. Identifier le modèle de données : **Catalogue, panier, prix figés par ligne, commande, paiement, remboursement, stock, facture et journal de statut**. Documenter chaque champ privé/public et la provenance des données.

## Procédure spécifique
4. **Parcours métier :** Dessiner une machine d’états commande/payment, séparer lecture publique et écritures privées, choisir stockage transactionnel, formaliser connecteur PSP; identifier les points non fournis par Éclair v2. Dessiner les états et les erreurs avant d'écrire du code.
5. **Emplacements :** conserver tout code propriétaire au site dans `site/extensions/<id>/`, l'apparence dans `site/themes/<id>/` ; enregistrer les données dans le préfixe `Store` fourni par `$ctx['data']`. Ne jamais éditer `app/`, `assets/`, `index.php` ou l'updater dans le cadre de ce skill.
6. **Contrat actuel :** Le noyau fournit déjà une boutique légère (fiches produit, variantes, catégories, liens de paiement d'un prestataire, flux marchand) : l'utiliser d'abord, sans la dupliquer. Au-delà, panier, commandes et paiements ont besoin de POST publics, d’un stockage transactionnel fiable, de webhooks authentifiés et d’idempotence; Éclair 2.0 officiel ne fournit pas tout cela. La PR #19 est encore un brouillon : ne jamais utiliser une route POST non fusionnée comme preuve de compatibilité.
7. **Invariant de sécurité :** Aucun paiement n’est déclaré réussi depuis la seule redirection navigateur; le serveur valide un événement PSP authentifié. Vérifier droits serveur sur chaque objet, échappement avec `e()`, validation des données, absence de secret et de PII dans le HTML public ou un cache partagé.
8. **Preuves :** écrire test positif « Simuler achat, confirmation webhook, réessai, remboursement, stock et annulation » et test de rejet « Même notification de paiement livrée deux fois => une seule transition de commande ». Mesurer les régressions SEO/performance, documenter rollback et responsabilité des données.
9. **Validation native :** `php tools/validate.php <dossier> --json`, `php tests/run.php` et `php tools/measure.php --check` sur le checkout officiel (si extension installable). Pour une fonctionnalité non supportée par le noyau actuel, fournir une RFC et un test bloquant, pas une assertion de réussite fictive.

## Livrables obligatoires
- Mini-spécification : objectifs, utilisateurs, parcours, états, données, métriques.
- Matrice d'autorisations et de cache : route, méthode, session, visibilité, indexation.
- Paquet `extension.json`/`extension.php` seulement si le contrat natif supporte réellement les opérations ; sinon plan d'extension ou maquette GET sûre.
- Tests démontrant les cas positifs et les refus, procédure de désactivation conservant les données et note de compatibilité.

## Critères d'acceptation
- Simuler achat, confirmation webhook, réessai, remboursement, stock et annulation.
- Même notification de paiement livrée deux fois => une seule transition de commande.
- Les parcours non pris en charge par Éclair v2 sont explicitement signalés comme **non livrables en production**.

**Statut de maturité de ce skill :** `design-workflow-requires-verified-core-capabilities`. Voir `references/acceptance.md` pour les cas d'essai reproductibles.
