# Plan de validación — Filtros y ordenación del catálogo

## Modelo de datos
Criterio, valor, combinación, dirección filtrada.

## Implementación esperada
Apoyarse en los filtros nativos por categoría; añadir filtros en el navegador sobre datos públicos, con direcciones canónicas controladas.

## Tests que deben preverse
1. Nominal: Filtrar y ordenar un catálogo de prueba en móvil.
2. Control de rechazo: Una combinación sin resultados muestra un mensaje, no una página vacía indexable.
3. Invariante: Las combinaciones de filtros no crean una infinidad de páginas indexables.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
