# Plan de validación — Reseñas de productos

## Modelo de datos
Reseña, valoración, autor, compra verificada, estado.

## Implementación esperada
Definir prueba de compra, moderación, derecho de réplica y visualización agregada; proponer mientras tanto testimonios recogidos manualmente.

## Tests que deben preverse
1. Nominal: Simular envío, moderación y publicación de una reseña.
2. Control de rechazo: Una reseña sin compra verificada no se marca como verificada.
3. Invariante: Ninguna reseña publicada sin moderación; ninguna valoración agregada sin reseñas reales.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
