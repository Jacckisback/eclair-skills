# Éclair Skills v1.2.0 — Release candidate expérimentale

## Évolutions

- `Member Directory v0.3.0` : inscription sur email uniquement, vérification d'email à usage unique et mot de passe choisi lors de la vérification.
- Récupération de compte : jeton 15 minutes, POST de changement de mot de passe, invalidation des anciennes sessions grâce à `epoch`.
- Liens de vérification 30 minutes, construits depuis `Settings::get('url')` après contrôle HTTPS + `Settings::verified()`, jamais via `HTTP_HOST`.
- Comptes membres dissociés des comptes CMS, permissions par sujet/session, aucun rôle administrateur issu d'un compte public.
- Anti-CSRF et limiteur central `RateLimit` pour les POST, erreurs génériques pour les demandes email.
- Inscription et récupération désactivées par défaut dans le manifeste de l'extension ; aucune mutation sur GET ; `cache:false` et `noindex`.
- En cas de rejet SMTP d'un nouvel email d'inscription, suppression contrôlée de l'entrée pending pour éviter le blocage permanent du compte.
- Patch expérimental public POST : autorise les réponses génériques `200`, en plus des erreurs, avec `Cache-Control: private, no-store`.
- Vérificateur du dépôt officiel `scripts/check_native_eclair.py` (non exécuté contre le dépôt officiel dans cet environnement).

## Risques non éliminés

L'envoi réel de l'email n'a pas été vérifié ; le retour booléen de `Mail::send` ne garantit pas la livraison dans la boîte du destinataire. La limitation des tentatives et les erreurs génériques n'éliminent pas toutes les possibilités d'énumération temporelle. Les jetons transmis en URL exigent une politique de confidentialité des logs/Referer. Le stockage sur plusieurs fichiers n'est pas entièrement transactionnel, et les tests de concurrence doivent être validés sur hébergement réel.

Ce kit est destiné à la revue de code et à l'expérimentation sous HTTPS, jamais à recevoir des comptes clients réels avant qualification de bout en bout.

- Défense TLS supplémentaire : refus de la confiance implicite en `X-Forwarded-Proto` et autorisation d'un proxy seulement par son adresse IP explicite (`ECLAIR_MEMBER_TRUSTED_PROXY_IP`).
