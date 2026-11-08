---
name: eclair-enrollment-access
description: "Use when a user wants to lier achat ou validation à une inscription et à ses autorisations on Éclair CMS 2.x; design a inscriptions aux cours workflow with native extension compatibility, security and acceptance gates."
---

# Inscriptions aux cours — Éclair CMS 2.x

## Déclencheur et résultat attendu
Utiliser ce skill pour **lier achat ou validation à une inscription et à ses autorisations**. Il produit une architecture vérifiable, les changements de site autorisés, des tests positifs et négatifs et une note sur les dépendances au noyau. Ce skill est un **workflow d'agent**, pas une extension PHP fonctionnelle ni une garantie de conformité.

## Diagnostic obligatoire avant modification
1. Lire `references/core-map.md` et `references/native-contract.md` ; vérifier version réelle du CMS, manifeste `eclair-extension/1` et les capacités disponibles dans `GET /<admin>/api/capabilities` (si accès autorisé).
2. Lire `references/family-contract.md` et `references/acceptance.md` pour ce domaine. Ne jamais copier l'ancien système de packs v0.x dans Éclair 2.
3. Identifier le modèle de données : **Membre, cours, inscription, état, origine, date et révocation**. Documenter chaque champ privé/public et la provenance des données.

## Procédure spécifique
4. **Parcours métier :** Créer inscription idempotente; traiter droits par objet; distinguer inscription gratuite/payant; révoquer après remboursement selon règle explicite. Dessiner les états et les erreurs avant d'écrire du code.
5. **Emplacements :** conserver tout code propriétaire au site dans `site/extensions/<id>/`, l'apparence dans `site/themes/<id>/` ; enregistrer les données dans le préfixe `Store` fourni par `$ctx['data']`. Ne jamais éditer `app/`, `assets/`, `index.php` ou l'updater dans le cadre de ce skill.
6. **Contrat actuel :** Les pages de présentation de cours peuvent être publiques GET. Les cours payants, progrès et évaluations nécessitent une identité membre qualifiée, des vérifications d’accès objet et des écritures privées non cacheables.
7. **Invariant de sécurité :** Jamais d’inscription automatique sur une simple URL de retour prestataire de paiement. Vérifier droits serveur sur chaque objet, échappement avec `e()`, validation des données, absence de secret et de PII dans le HTML public ou un cache partagé.
8. **Preuves :** écrire test positif « Tester double achat, remboursement, suspension du compte » et test de rejet « Un membre radié ne peut plus accéder aux leçons auparavant autorisées ». Mesurer les régressions SEO/performance, documenter rollback et responsabilité des données.
9. **Validation native :** `php tools/validate.php <dossier> --json`, `php tests/run.php` et `php tools/measure.php --check` sur le checkout officiel (si extension installable). Pour une fonctionnalité non supportée par le noyau actuel, fournir une RFC et un test bloquant, pas une assertion de réussite fictive.

## Livrables obligatoires
- Mini-spécification : objectifs, utilisateurs, parcours, états, données, métriques.
- Matrice d'autorisations et de cache : route, méthode, session, visibilité, indexation.
- Paquet `extension.json`/`extension.php` seulement si le contrat natif supporte réellement les opérations ; sinon plan d'extension ou maquette GET sûre.
- Tests démontrant les cas positifs et les refus, procédure de désactivation conservant les données et note de compatibilité.

## Critères d'acceptation
- Tester double achat, remboursement, suspension du compte.
- Un membre radié ne peut plus accéder aux leçons auparavant autorisées.
- Les parcours non pris en charge par Éclair v2 sont explicitement signalés comme **non livrables en production**.

**Statut de maturité de ce skill :** `design-workflow-requires-verified-core-capabilities`. Voir `references/acceptance.md` pour les cas d'essai reproductibles.
