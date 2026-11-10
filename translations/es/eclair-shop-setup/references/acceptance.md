# Plan de validación — Apertura de la tienda ligera

## Modelo de datos
Producto, precio, categoría, aviso legal, condiciones de venta.

## Implementación esperada
Publicar el aviso legal y las condiciones de venta, abrir la tienda, crear las primeras fichas, comprobar el catálogo y los datos estructurados.

## Tests que deben preverse
1. Nominal: Abrir la tienda en una copia y recorrer el catálogo y una ficha.
2. Control de rechazo: La tienda no se abre sin páginas legales publicadas.
3. Invariante: Ningún precio, plazo o condición de venta inventados por el agente.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
