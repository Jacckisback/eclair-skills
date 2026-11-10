# Plan de validación — Stock y reservas

## Modelo de datos
SKU, almacén, stock físico, reservado, disponible, movimientos inmutables.

## Implementación esperada
Diseñar los movimientos de entrada/salida; bloquear la reserva; gestionar la expiración y la compensación; trazar todas las correcciones manuales.

## Tests que deben preverse
1. Nominal: Probar compras simultáneas de la última unidad y la liberación tras la expiración.
2. Control de rechazo: Dos compradores no pueden reservar la misma última unidad en stock.
3. Invariante: La lectura cacheable de la disponibilidad es informativa; toda venta vuelve a leer el stock dentro de una transacción.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
