# Public member HTTP routes — Éclair 2.0.0 experimental

Le stockage du démonstrateur utilise encore les fichiers protégés de `Store` et un verrou global. Il est borné à 1000 comptes; aucune promesse d’atomicité multi-fichiers, d’accès à grande échelle ou de tolérance aux pannes transactionnelles. Un backend SQL est un prérequis avant exploitation métier.

Le patch source se trouve dans `core-patch/` de la distribution complète, non inclus dans une copie autonome du skill. Ne jamais considérer ce patch comme une API officielle avant sa fusion upstream.
