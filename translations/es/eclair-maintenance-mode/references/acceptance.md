# Plan de validación — Modo de mantenimiento

## Modelo de datos
Estado de mantenimiento, mensaje, duración prevista, acceso del equipo.

## Implementación esperada
Servir una página estática con el código de estado HTTP temporal correcto a nivel del servidor, mantener el acceso a la administración, prever la vuelta a la puesta en línea.

## Tests que deben preverse
1. Nominal: Activar, verificar el estado 503 y la cabecera de reintento, desactivar.
2. Control de rechazo: Los robots nunca reciben la página de mantenimiento con un estado 200.
3. Invariante: La página de mantenimiento no revela ni la versión ni la ruta del servidor.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
