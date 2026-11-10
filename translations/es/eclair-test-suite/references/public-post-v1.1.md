# Public member HTTP routes — Éclair 2.0.0 experimental

Probar `php tests/member-directory.php` + `php tests/member-public.php` y los tests de Python. En un clon real de Éclair 2.0.0, aplicar el patch a una feature branch limpia, ejecutar `php tools/validate.php`, `php tests/run.php`, `php tools/measure.php --check` y pruebas HTTP/TLS. Ninguna fusión sin estos criterios.

El patch fuente se encuentra en `core-patch/` de la distribución completa, no incluido en una copia autónoma del skill. No considerar nunca este patch como una API oficial antes de su fusión upstream.
