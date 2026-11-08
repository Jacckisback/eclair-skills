> **Statut actualisé v1.1.0 :** voir `PUBLIC_POST_RFC.md` pour la première implémentation expérimentale des routes POST et le parcours connexion/espace/déconnexion. Inscription, invitation email et récupération de mot de passe restent hors périmètre du prototype.

# RFC-1 — Public Member Identity for Éclair CMS 2.0

Statut: PROPOSITION, PAS UNE API EXISTANTE.

## Constat confirmé dans le noyau officiel (2026-11-08)
- `eclair-extension/1`: routes publiques **GET seulement**; routes d'administration GET/POST avec `right`.
- `Auth/Users` couvrent l'administration, et **ne doivent jamais** servir de base de comptes clients.
- Pages publiques statiques servies très vite via `index.php`; ne jamais les employer pour une session membre.
- Le validateur officiel est `php tools/validate.php <dossier>` ; le schéma natif se trouve sous `docs/schemas/extension.schema.json`.

## Contrat cible (à discuter avant codage noyau)
1. Introduire `member-route/1` (ou extension mineure de `eclair-extension`) pour déclarer explicitement `GET|POST` publics, cache `private/no-store` obligatoire pour toute session, routes non mises en cache par le fast path.
2. Séparer `Auth` (admin) de `MemberIdentity` (visiteurs) ; les cookies `__Host-` Secure+HttpOnly+SameSite si domaine HTTPS. Refuser HTTP pour sessions.
3. Enregistrement de membres: normalisation d'email, hachage Argon2id/bcrypt, vérification email à usage unique avec expiry, rate limiting par compte/IP, responses non énumérables, CAPTCHA adaptable.
4. Autres endpoints: login, logout, reset request, reset confirm, verify email; exiger CSRF pour les actions basées sur cookies, `Origin/Sec-Fetch-Site` et protections anti login-CSRF; pas d'effets de bord sur GET.
5. Autoriser des policies par module avec scope `own/any` sur objets métier, jamais seulement sur rôle.
6. Migrations et stockage: garanties transactionnelles pour index/email/session token sur un moteur adapté, pas simple promesse de transaction multi-fichiers.
7. Publication: validation manuelle par un administrateur, journaux minimaux, sauvegarde sans sessions/secrets; revue de conformité RGPD selon le projet.

## Critères bloquants de merge
- Scénarios HTTP sur TLS, cookie sécurisé, 401/403, CSRF, Origin, IDOR, session fixation, révocation, timing compte inconnu, login brute-force.
- Tests concurrence + panne lors d'une création et réinitialisation sur le backend de données promis.
- Test de non-régression du chemin rapide `index.php`, budgets mémoire/latence, SEO/GEO inchangés pour les pages publiques.
- Toutes les suites officielles `php tests/run.php` et `php tools/measure.php --check` sur sources et build, PHP 8.1 à 8.5.

## Statut du démonstrateur v1.0
Le module `examples/extensions/member-directory` expose seulement une interface d'**administrateur**. Les comptes commencent `pending`. Il ne propose aucune connexion publique, ne transmet aucun email et n'est pas prêt à prendre en charge des clients réels. Les services de session sont une référence expérimentale et ne sont pas raccordés au HTTP public.


> **Mise à jour v1.2** — Voir `MEMBER_EMAIL_V12.md` pour les nouveaux parcours (inscription/vérification/récupération désactivés par défaut), `NATIVE_VALIDATION_RUNBOOK.md` pour les critères de mise en production. Le contrat public POST reste un prototype non fusionné.
