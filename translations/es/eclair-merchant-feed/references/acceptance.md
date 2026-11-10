# Plan de validación — Feed de productos

## Modelo de datos
Producto, precio, disponibilidad, imagen, identificadores.

## Implementación esperada
Completar las fichas, controlar el feed generado por el núcleo, declararlo en la herramienta para comerciantes, corregir los rechazos.

## Tests que deben preverse
1. Nominal: Validar el feed y comparar tres productos con su ficha.
2. Control de rechazo: Un producto no disponible no se anuncia como en stock.
3. Invariante: El precio y la disponibilidad del feed son los de la ficha pública.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
