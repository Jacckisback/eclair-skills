# Public member HTTP routes — Éclair 2.0.0 experimental

Le prototype v1.1 a une limitation `RateLimit::attempt` avant hash, une séparation stricte membres/admin et des jetons de session 256 bits. Évaluer la sécurité des `Origin`, de TLS derrière reverse proxy, CSRF, IDOR, énumération de comptes, fuites d’informations et concurrence. Ne pas confondre tests isolés et audit en production.

Le patch source se trouve dans `core-patch/` de la distribution complète, non inclus dans une copie autonome du skill. Ne jamais considérer ce patch comme une API officielle avant sa fusion upstream.
