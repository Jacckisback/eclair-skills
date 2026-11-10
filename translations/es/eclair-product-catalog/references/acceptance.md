# Plan de validación — Catálogo de productos

## Modelo de datos
Producto, SKU, slug, título, descripción, precio de presentación, medio, disponibilidad y categoría.

## Implementación esperada
Prototipar primero una página pública GET cacheable; producir un esquema de producto y su índice; mantener los títulos y descripciones de origen; definir paginación y canonical; preservar los slugs a lo largo de las ediciones.

## Tests que deben preverse
1. Nominal: Probar categorías, listados vacíos, URL canónica, búsqueda y eliminación soft.
2. Control de rechazo: Un producto eliminado o privado no debe permanecer en el catálogo ni en una caché antigua.
3. Invariante: El precio mostrado nunca se toma como fuente de autoridad en un pedido futuro.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
