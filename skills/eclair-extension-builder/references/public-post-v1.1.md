# Public member HTTP routes — Éclair 2.0.0 experimental

Un prototype de route POST publique figure dans `examples/extensions/member-directory/`. Il est rejeté par le noyau 2.0 officiel. N’utiliser le manifeste qu’avec le patch expérimental et l’accord explicite d’un mainteneur, jamais en production. POST exige `cache:false`, TLS, CSRF, redirection relative.

Le patch source se trouve dans `core-patch/` de la distribution complète, non inclus dans une copie autonome du skill. Ne jamais considérer ce patch comme une API officielle avant sa fusion upstream.
