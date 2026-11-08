# RFC-2 — Public POST extension endpoints (experimental)

État : prototype local, **non fusionné**.

## Problème
Le contrat officiel `eclair-extension/1` n'autorise que GET pour les routes publiques; les routes administrateur autorisent GET/POST. Le noyau 2.0 ne propose pas d'inscription ou de connexion publique pour des membres distincts des admins.

## Proposition minimale
- `routes.public[].method` peut prendre GET ou POST.
- POST impose `cache:false`, TLS, validation stateless CSRF par `Security::checkFormToken()`, `Origin` et `Sec-Fetch-Site` via le noyau.
- Réponses POST `private, no-store` et `noindex,nofollow` ; redirection uniquement vers des chemins locaux avec 303.
- GET portant un formulaire ou des informations membres doit rester `cache:false`, `noindex`; ne jamais publier un jeton ou l'email d'un membre sur une page cachée.
- Le code PHP d'extension conserve la responsabilité d'autoriser l'objet métier et de limiter les tentatives (RateLimit).

## Démonstrateur du module Member Directory v0.2
- GET `/membres/connexion`: formulaire non caché avec jeton anti-CSRF stateless.
- POST `/membres/connexion`: HTTPS + CSRF + double limitation (IP / compte), authentifie seulement les comptes `active`, renouvelle une session isolée.
- GET `/membres/espace`: lecture de sa propre identité depuis cookie de membre validé, `noindex`, formulaire de déconnexion.
- POST `/membres/deconnexion`: HTTPS + CSRF formulaire + CSRF lié à la session membre, révoque et efface le cookie.
- **Aucun endpoint public d'inscription** : invitation/vérification email et récupération de compte devront être traitées dans une autre étape, avec livraison email vérifiée et tests de concurrence.

## Critères avant merge
1. Validateur natif du CMS (`php tools/validate.php`) passe sur le module avec le patch; tests HTTP réels avec TLS et cookies.
2. Tests du noyau (`php tests/run.php`), de son build et budgets (`php tools/measure.php --check`) passent sur versions PHP 8.1–8.5.
3. Tests non-régression : aucun effet de bord sur GET, aucun POST dans le cache, CSRF cross-origin 419, HTTP 403, cookies `__Host-` Secure, compte pending refusé, login admin inaccessible, throttling, objets d'autres membres interdits.
4. Audit des erreurs et de la configuration reverse proxy; mécanisme mail et base transactionnelle avant usage réel.


> **Mise à jour v1.2** — Voir `MEMBER_EMAIL_V12.md` pour les nouveaux parcours (inscription/vérification/récupération désactivés par défaut), `NATIVE_VALIDATION_RUNBOOK.md` pour les critères de mise en production. Le contrat public POST reste un prototype non fusionné.
