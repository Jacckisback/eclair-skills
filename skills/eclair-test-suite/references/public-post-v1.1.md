# Public member HTTP routes — Éclair 2.0.0 experimental

Tester `php tests/member-directory.php` + `php tests/member-public.php` et les tests Python. Sur un vrai clone Éclair 2.0.0, appliquer le patch à une feature branch propre, faire `php tools/validate.php`, `php tests/run.php`, `php tools/measure.php --check`, et des essais HTTP/TLS. Aucune fusion sans ces critères.

Le patch source se trouve dans `core-patch/` de la distribution complète, non inclus dans une copie autonome du skill. Ne jamais considérer ce patch comme une API officielle avant sa fusion upstream.
