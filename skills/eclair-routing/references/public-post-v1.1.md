# Public member HTTP routes — Éclair 2.0.0 experimental

Les routes publiques POST ne sont **pas** présentes dans Éclair 2.0 officiel. Le patch proposé v1.1 fait une exception contrôlée : méthode POST explicite, `cache:false`, HTTPS, `Security::checkFormToken()`, réponse `private,no-store`, redirection 303 relative. Toujours faire des essais HTTP avec le CMS complet avant fusion.

Le patch source se trouve dans `core-patch/` de la distribution complète, non inclus dans une copie autonome du skill. Ne jamais considérer ce patch comme une API officielle avant sa fusion upstream.
