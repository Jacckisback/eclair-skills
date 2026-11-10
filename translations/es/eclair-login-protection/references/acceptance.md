# Plan de validación — Protección del inicio de sesión

## Modelo de datos
Intentos, límites por red y por cuenta, dirección de administración.

## Implementación esperada
Comprobar los límites de intentos nativos, la dirección de administración, las sesiones activas y las contraseñas provisionales.

## Tests que deben preverse
1. Nominal: Simular fallos repetidos y comprobar el bloqueo.
2. Control de rechazo: El dispositivo habitual del propietario no queda bloqueado por los intentos de un tercero.
3. Invariante: Ningún límite nativo se relaja.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
