# Public member HTTP routes — Éclair 2.0.0 experimental

`php tests/member-directory.php` + `php tests/member-public.php` sowie die Python-Tests ausführen. Auf einem echten Klon von Éclair 2.0.0 den Patch auf einen sauberen Feature-Branch anwenden, `php tools/validate.php`, `php tests/run.php`, `php tools/measure.php --check` sowie HTTP/TLS-Tests durchführen. Kein Merge ohne diese Kriterien.

Der Quell-Patch liegt in `core-patch/` der vollständigen Distribution und ist in einer eigenständigen Kopie des Skills nicht enthalten. Diesen Patch niemals als offizielle API betrachten, bevor er upstream gemergt ist.
