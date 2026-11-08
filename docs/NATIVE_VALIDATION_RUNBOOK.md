# Vérifier réellement Éclair v2 + Member Directory v0.3.0

**Statut : à exécuter.** Les simulations du kit ne remplacent jamais le validateur officiel du CMS.

## 0 — Gel d'une version et préparation

1. Travailler dans un clone de `https://github.com/Jacckisback/eclair-cms` à la version **2.0.0** vérifiée (`eclair/index.php`), et relever son commit. Si le code a changé, ne pas forcer la pose du patch : refaire une analyse.
2. Créer une branche Git de développement propre (non `main`, non `master`), puis consulter le diff avant de fusionner.
3. Vérifier que `php -v` et les extensions indispensables du CMS sont disponibles ; pour l'intégration SQL future, `pdo_sqlite` sera nécessaire, mais pas pour le modèle actuel en fichiers.

## 1 — Patch contrôlé (non destructif avant --apply)

```bash
python3 /chemin/eclair-skills-v1.2.0/core-patch/apply_public_post.py --checkout .
python3 /chemin/eclair-skills-v1.2.0/core-patch/apply_public_post.py --checkout . --apply
git diff --check
git diff -- eclair/app/lib/Extensions.php docs/schemas/extension.schema.json
```

Le patch n'est pas officiellement fusionné. Il doit être refusé si la version, l'ancre de code ou l'état du dépôt diffère. **N'appliquer qu'à la branche locale**.

## 2 — Validateur, tests et budgets officiels

```bash
EXT=/chemin/eclair-skills-v1.2.0/examples/extensions/member-directory
php tools/validate.php "$EXT" --json
php tests/run.php
php tools/measure.php --check
python3 /chemin/eclair-skills-v1.2.0/scripts/check_native_eclair.py --checkout . --report /tmp/eclair-auth-gates.json
```

L'ensemble de ces commandes doit réussir. Vérifier également le build sur l'archive distribuable et une matrice PHP 8.1, 8.2, 8.3, 8.4, 8.5 en CI. Un changement de comportement de `tools/measure.php` impose de comparer les mesures avec une baseline reproduite.

## 3 — Serveurs et parcours sensibles (manuels/automatisés)

- HTTPS strict : refus des POST sur HTTP, y compris avec `X-Forwarded-Proto: https` provenant d’une IP non approuvée, et configuration explicite de `ECLAIR_MEMBER_TRUSTED_PROXY_IP` si nécessaire ; cookies membres `__Host-eclair_member` `Secure` `HttpOnly` `SameSite=Lax`, `Path=/`, indépendants du cookie admin.
- Inscription désactivée par défaut, récupération désactivée par défaut et échec si URL canonique HTTPS non vérifiée.
- Formulaire GET + POST uniquement, origine et CSRF vérifiés, jamais de mutation d'état sur GET ; pas de cache public ni CDN pour les pages personnelles et les formulaires.
- Nouvelle inscription → email reçu → lien utilisable une seule fois → mot de passe défini par l'utilisateur → connexion ; vérification et réinitialisation après expiration refusées.
- Réinitialisation : même réponse visible pour adresse inconnue ou existante, tentatives limitées par IP et adresse, sessions précédentes invalidées.
- Erreurs SMTP : compte pending provisoire nettoyé si transport refuse la soumission ; en cas de mail remis mais non reçu, prévoir récupération assistée.
- Profil membre A ne révèle jamais les informations du membre B, et aucun membre ne devient admin/editor, même en forgeant des rôles ou un cookie.
- Révocation lors de la désactivation du compte ; logout CSRF lié à la session.
- Contrôles rate limiting sous concurrence et charge, abus d'inscription et email bombing, résistance à l'énumération par **timing**, consommation mémoire, réponse à une panne disque.
- Prévention des fuites de jetons via journaux, Referer, historiques navigateur et actifs externes sur les pages de vérification.

## 4 — Exigences de fusion

N'autoriser ni merge ni déploiement réel sans les tests de l'étape 2, HTTPS et SMTP de l'étape 3, revue de sécurité indépendante, stratégie RGPD (rétention/effacement), export/sauvegarde/restauration, rollback et profil de performances. Définir une voie de recovery des comptes en attente si l'email n'a pas été livré. Prévoir une base transactionnelle si le produit doit gérer commandes, formations ou communauté à grande échelle.
