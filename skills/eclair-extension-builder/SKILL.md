---
name: eclair-extension-builder
description: Use when creating or adapting an Éclair CMS 2.0 optional server extension that uses extension.json, extension.php and the native eclair-extension/1 contract.
---

# Éclair Extension Builder — bâtir une fonction réellement installable en v2

## Objectif
Créer un **paquet `eclair-extension/1` conforme au noyau v2**. Ne pas utiliser le manifeste `manifest.json` ou les fichiers `events.php` / `services.php` des anciens prototypes comme s'ils étaient supportés.

## Processus
1. Lire `references/core-map.md`, `docs/EXTENSION-CONTRACT.md`, `docs/schemas/extension.schema.json` et `examples/extensions/bonjour` du checkout.
2. Vérifier `ECLAIR_VERSION` et le contrat `eclair-extension/1` par le code et, si accessible, l'API des capacités.
3. Définir `id`, `version`, `requires`, `depends`, `provides`, `entry`, routes, blocs, champs, assets, `tasks`, migrations ; utiliser uniquement les champs du schéma.
4. Livrer dans `site/extensions/<id>/` **sans écrire dans `app/`** ; l'entrée PHP doit renvoyer un objet et ne doit rien produire lors de son chargement.
5. Contrôler l'affichage avec `e()` ; lire les réglages depuis `$ctx['settings']` ; stocker via `Eclair\Store` sous `$ctx['data']`. Pour les secrets : emplacement privé et politique de non-sauvegarde documentée.
6. Routes publiques GET seulement. Sur une page publique qui affiche une donnée de session ou individuelle : arrêt et demande de nouveau contrat d'identité/cache ; pas de faux contournement.
7. Calculer les SHA-256 des fichiers et les déclarer dans `files`, sauf `extension.json`. Générer un paquet ZIP dont la racine contient le manifeste.
8. `php tools/validate.php chemin/extension --json` ; corriger toutes les erreurs avant de proposer l'import, puis tester `php tests/run.php` et `php tools/measure.php --check`.
9. Une personne autorisée importe, prévisualise/contrôle, active ; documenter la désactivation, la suppression de code et la conservation des données.

## Livrables
`extension.json`, entrée `extension.php`, références, tests, preuve de validation officielle et manuel d'installation. Exemple original dans `examples/extensions/skill-sample/` ; vérifier sur le noyau exact avant déploiement.

## V1.0 — Modèle avancé livré
Consulter `examples/extensions/member-directory` : il prouve des routes admin GET/POST natives et une bibliothèque PHP chargée seulement par l'extension. Ne pas transformer son GET admin en connexion publique ni ajouter un POST à `routes.public` (contrat v2 incompatible).

## Éclair 2.0 — prototype v1.1 (experimental)
Un prototype de route POST publique figure dans `examples/extensions/member-directory/`. Il est rejeté par le noyau 2.0 officiel. N’utiliser le manifeste qu’avec le patch expérimental et l’accord explicite d’un mainteneur, jamais en production. POST exige `cache:false`, TLS, CSRF, redirection relative.

## Éclair 2.0 — inscription et récupération (v1.2 expérimentale)

Lire `references/member-email-v1.2.md` avant toute demande de création de comptes clients/élèves ou de récupération de mot de passe. Le module `member-directory` v0.3 utilise des routes publiques POST **hors contrat officiel** ; ne jamais promettre une installation directe sur Éclair 2.0 non modifié ni activer les flux email sans URL HTTPS vérifiée et tests natifs. Préférer le système d'extensions v2 à toute modification de l'ancienne architecture v0.x. Garder séparés les comptes publics et administrateurs, refuser tout cache partagé pour les pages membres, et traiter les emails comme non livrés tant qu'aucune confirmation n'existe.
