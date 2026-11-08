# Public member HTTP routes — Éclair 2.0.0 experimental

Les formulaires publics GET utilisent `Security::formField()` et doivent être déclarés `cache:false`. Leurs réponses ne doivent pas atteindre le fast path du noyau. POST est exclu du fast path et forcé no-store. Tester la purge à l’activation du module et vérifier l’absence de cookies/identités dans le HTML de cache partagé.

Le patch source se trouve dans `core-patch/` de la distribution complète, non inclus dans une copie autonome du skill. Ne jamais considérer ce patch comme une API officielle avant sa fusion upstream.
