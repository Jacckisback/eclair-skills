# Plan de validación — Cuentas atrás

## Modelo de datos
Fecha objetivo, zona horaria, mensaje de finalización.

## Implementación esperada
Escribir la fecha en el HTML, animar como mejora progresiva, prever el estado tras el vencimiento y la invalidación de la caché.

## Tests que deben preverse
1. Nominal: Probar antes, durante y después del vencimiento y en dos zonas horarias.
2. Control de rechazo: Tras el vencimiento, la página en caché ya no muestra ninguna oferta caducada.
3. Invariante: Ninguna falsa urgencia: la fecha corresponde a un evento real.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
