# Éclair Member Directory — v1.0 reference

Un démonstrateur natif Éclair 2.0 est fourni dans `examples/extensions/member-directory/` à la racine de la distribution source ; il n'est pas inclus lors de la copie autonome du skill.

- `schema`: `eclair-extension/1` ; `requires.eclair`: `>=2.0.0`.
- Routes `admin`: GET racine, POST `/create`, POST `/disable` ; droit `users`.
- Aucune route publique. Aucun login public et aucun email de validation n'est envoyé.
- `Store` : clés `ext/member-directory/...`, écriture sous verrou, limite 1 000 membres à titre expérimental.
- Session membre distincte des sessions de l'administration, jeton opaque 256 bits haché au repos, révocation par epoch.
- Activation après preuve d'email : non fournie par la surface HTTP. Un rôle membre ne peut pas être `admin` ou `editor`.
- Installateur: copier l'extension vers `site/extensions/member-directory`, passer `tools/validate.php` du noyau 2.0, importer et activer manuellement seulement en laboratoire.
- Pour des comptes actifs destinés au public : RFC pour POST public sûr, validation d'email, rate limiting, flux de reset et tests natifs. Aucune route GET ne doit créer/modifier un compte ou une session.
