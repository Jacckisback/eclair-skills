# Plan de validación — Testimonios y opiniones

## Modelo de datos
Testimonio, autor, fecha, autorización.

## Implementación esperada
Recoger los testimonios reales con autorización escrita, presentarlos como citas, indicar la fuente.

## Tests que deben preverse
1. Nominal: Comprobar que cada testimonio publicado tiene una autorización registrada.
2. Control de rechazo: Una opinión sin fuente verificable no se publica.
3. Invariante: Ninguna opinión inventada, modificada o seleccionada de forma engañosa.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
