---
name: eclair-auth-roles
description: Use when reviewing Éclair v2 admin rights or designing member, student, customer and moderator authentication beyond the admin-only built-in roles.
---

# Éclair Auth & Roles — distinguer admin et membres

## Réalité v2
`Eclair\Auth` et `Users` contrôlent **l'administration** avec ses droits (`content`, `settings`, `security`, etc.). Ils ne sont pas un annuaire clients, élèves ou membres, et ne doivent pas être détournés en rôles `customer/student`.

## Procédure
1. Consulter `Users`, `Auth`, `Admin`, `Security`, `Session`, `RateLimit` et le droit demandé par chaque route admin `eclair-extension/1`.
2. Pour une fonction d'administration, déclarer `routes.admin[]` avec `right` exact et s'appuyer sur la vérification CSRF du noyau. Vérifier l'accès selon chaque rôle existant.
3. Pour un espace public clients/élèves : produire une RFC de fournisseur d'identité ou un composant serveur dédié et audité avec stockage adapté ; **ne pas** exposer les routes sensibles via GET public.
4. Définir la session membre indépendante, les cookies `Secure/HttpOnly/SameSite`, les authentifications progressives, rate limiting, récupération et vérification email.
5. Permissions : systématiquement identifier le sujet via une session serveur vérifiée, puis contrôler l'objet et la portée (IDOR/BOLA) à chaque requête.
6. Tester absence de privilèges hérités de l'admin, changement de rôle, révocation, reset, courses de sessions, accès inter-comptes, CSRF et refus par défaut.

## Démonstrateur natif v1.0
La fonction `examples/extensions/member-directory/` fournit un exemple **admin seulement** pour Éclair 2.0 :
- `routes.admin`: GET + POST (`users`) avec contrôles renforcés dans les handlers ; `routes.public`: tableau vide.
- `MemberAccounts` et `MemberSessions` restent indépendants de `Eclair\Users/Auth/Session` ; compte `pending` obligatoire au provisionnement.
- Les données résident exclusivement sous `data/ext/member-directory/` via `Store`. Jamais dans `data/users.php`.
- `MemberPermissions::allows` prend un jeton de session vérifié, pas une identité fournie par l'appelant.
- Ni inscription publique, ni email envoyé, ni récupération de mot de passe, ni gestion réelle des sessions HTTP n'est activée.
- L'API POST publique nécessite une RFC/nouveau contrat du noyau et une validation de bout en bout avant déploiement.
Lire `references/member-directory-v1.md` avant de construire un LMS, forum ou commerce.

## Livrables
Matrice permissions et ressources, modèle de menaces, plan d'identité, jeux de tests et indication « native / RFC requise ».

## Éclair 2.0 — prototype v1.1 (experimental)
Le prototype v1.1 possède des handlers publics GET formulaire + POST connexion/déconnexion + GET espace privé. Ils ne sont valides qu’après l’ajout approuvé du contrat POST. Sessions membres distinctes des admins, jeton opaque, CSRF double-submit et CSRF de session à la déconnexion; aucun rôle admin/editor accordé.

## Éclair 2.0 — inscription et récupération (v1.2 expérimentale)

Lire `references/member-email-v1.2.md` avant toute demande de création de comptes clients/élèves ou de récupération de mot de passe. Le module `member-directory` v0.3 utilise des routes publiques POST **hors contrat officiel** ; ne jamais promettre une installation directe sur Éclair 2.0 non modifié ni activer les flux email sans URL HTTPS vérifiée et tests natifs. Préférer le système d'extensions v2 à toute modification de l'ancienne architecture v0.x. Garder séparés les comptes publics et administrateurs, refuser tout cache partagé pour les pages membres, et traiter les emails comme non livrés tant qu'aucune confirmation n'existe.
