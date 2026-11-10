# Plan de validación — Feeds de calendario

## Modelo de datos
Evento, fecha, zona horaria, lugar, feed iCalendar.

## Implementación esperada
Generar un feed iCalendar público en GET a partir de los eventos publicados, con zonas horarias explícitas.

## Tests que deben preverse
1. Nominal: Suscribirse al feed desde dos aplicaciones de calendario.
2. Control de rechazo: Un evento cancelado se marca como cancelado en el feed.
3. Invariante: El feed solo contiene eventos públicos, sin participantes.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
