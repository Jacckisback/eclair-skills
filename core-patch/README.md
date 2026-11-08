# Patch expérimental de routes POST publiques — Éclair CMS 2.0.0 (Skills v1.2)

**Non intégré au CMS officiel et non qualifié production.** Ce patch modifie exactement `eclair/app/lib/Extensions.php` et `docs/schemas/extension.schema.json` dans un checkout 2.0.0 sur une branche Git propre, jamais `main/master`.

Le contrat natif `eclair-extension/1` est étendu pour accepter explicitement `routes.public[].method=POST`, uniquement avec `cache:false`. La route refuse par défaut toute demande non transportée via TLS direct. Un reverse proxy terminant TLS ne peut être déclaré fiable que par **adresse IP exacte** en configurant le paramètre administrateur côté serveur :

```php
// Dans le fichier de configuration serveur, hors de toute zone éditable par les visiteurs :
define('ECLAIR_MEMBER_TRUSTED_PROXY_IP', '192.0.2.10'); // exemple : remplacer par l'IP réelle du proxy
```

Le proxy doit impérativement remplacer l'en-tête client `X-Forwarded-Proto` ; un simple en-tête fourni par un visiteur n'est pas une preuve TLS. Le noyau expérimental et l'extension Member Directory v0.3 vérifient cette règle. L'adresse IP du proxy doit être vérifiée par l'opérateur avant tout activation.

POST vérifie `Security::checkFormToken()` (y compris l'origine), répond avec `Cache-Control: private, no-store`, `X-Robots-Tag: noindex, nofollow` et redirige via un chemin local strict avec 303. Les réponses génériques `200` peuvent être retournées sans révéler si un compte existe. Les GET privés doivent être déclarés `cache:false` et `noindex`.

## Commandes sur un checkout officiel local en développement

```bash
git switch -c feat/eclair-public-members-v12
python3 /chemin/eclair-skills-v1.2.0/core-patch/apply_public_post.py --checkout .
# Après inspection des changements attendus :
python3 /chemin/eclair-skills-v1.2.0/core-patch/apply_public_post.py --checkout . --apply
python3 /chemin/eclair-skills-v1.2.0/scripts/check_native_eclair.py --checkout .
```

L'outil refuse une version différente de 2.0.0, une branche principale, un checkout modifié ou des ancres de code différentes des sources auditées. Ne fusionner et ne déployer qu'après validation native et audit de sécurité du code.
