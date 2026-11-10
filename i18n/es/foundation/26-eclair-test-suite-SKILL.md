---
name: eclair-test-suite
description: Use when creating CI, regression, security and performance tests for Éclair CMS 2.0 themes, native extensions and advanced module integrations.
---

# Éclair Test Suite — una prueba antes de la publicación

## Orden de verificación
1. Anotar el commit y el `ECLAIR_VERSION`; exigir el contrato v2 oficial. Sin un checkout completo, limitar la afirmación a los tests realmente ejecutables.
2. `php -l` de cada PHP producido y después `php tools/validate.php site/extensions/<id> --json` con el núcleo correspondiente.
3. `php tests/run.php --unit`, después `php tests/run.php` (HTTP, auth, rutas, caché, copias de seguridad, extensiones, temas, migración de WordPress).
4. `php tools/measure.php --check`; comparar la caché caliente y el presupuesto de memoria/tiempo con el núcleo sin modificar.
5. Probar instalación inactiva, activación, migración idempotente, update, conflicto de ruta, desactivación, conservación de los datos, eliminación del código y eventual purga manual.
6. Si hay cuentas de miembros/SQL: exigir tests PHP/PDO reales, multiproceso, autorizaciones por objeto, webhooks firmados y restauración desde una copia de seguridad. `pdo_sqlite` ausente = test bloqueado, no superado.
7. CI recomendada: matriz PHP 8.1 a 8.5, `tests.yml` oficial, archivo construido y servidores Apache/Nginx; añadir jobs específicos de la funcionalidad.
8. Elaborar una tabla de tests ejecutados / fallidos / bloqueados. No informar nunca «compatible con producción» a partir de una fixture aislada.

## Entregables
Scripts y fixtures, informe de ejecución, cobertura de los casos adversos, presupuestos y estrategia de rollback.

## V1.0 — Verificaciones adicionales
Ejecutar `php tests/member-directory.php`, `python3 -m unittest discover -s tests -v` y `python3 scripts/verify_sample.py`. En un checkout completo de Éclair 2.0, ejecutar **obligatoriamente** `php tools/validate.php examples/extensions/member-directory --json` y después los tests PHP/HTTP del CMS completo y el presupuesto `tools/measure.php --check` antes de cualquier propuesta de fusión.

## Éclair 2.0 — prototipo v1.1 (experimental)
Probar `php tests/member-directory.php` + `php tests/member-public.php` y los tests de Python. En un clon real de Éclair 2.0.0, aplicar el patch a una feature branch limpia, ejecutar `php tools/validate.php`, `php tests/run.php`, `php tools/measure.php --check` y pruebas HTTP/TLS. Ninguna fusión sin estos criterios.

## Éclair 2.0 — registro y recuperación (v1.2 experimental)

Leer `references/member-email-v1.2.md` antes de cualquier petición de creación de cuentas de clientes/alumnos o de recuperación de contraseña. El módulo `member-directory` v0.3 utiliza rutas públicas POST **fuera del contrato oficial**; no prometer nunca una instalación directa en un Éclair 2.0 sin modificar ni activar los flujos de email sin una URL HTTPS verificada y tests nativos. Preferir el sistema de extensiones v2 a cualquier modificación de la antigua arquitectura v0.x. Mantener separadas las cuentas públicas y las de administración, rechazar toda caché compartida para las páginas de miembros y tratar los emails como no entregados mientras no exista ninguna confirmación.
