# Plan de validación — Cookies y consentimiento

## Modelo de datos
Rastreador, finalidad, consentimiento, prueba.

## Implementación esperada
Inventariar los rastreadores reales; sin rastreador, no hay banner; si no, consentimiento previo, rechazo tan sencillo como la aceptación y página de información.

## Tests que deben preverse
1. Nominal: Inspeccionar cookies y peticiones antes y después de la elección.
2. Control de rechazo: Tras un rechazo, no se carga ningún rastreador de terceros.
3. Invariante: Ningún rastreador sujeto a consentimiento se instala antes de la aceptación.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
