# Plan de validación — IVA y facturación

## Modelo de datos
País de venta y de entrega, localización fiscal, tipo impositivo vigente, factura, factura rectificativa, secuencia.

## Implementación esperada
Enumerar las jurisdicciones y los tipos de clientes; consultar las normas actualizadas y el asesoramiento contable; fijar la base imponible/el tipo en el momento del pedido; preparar exportaciones de facturas y facturas rectificativas.

## Tests que deben preverse
1. Nominal: Probar venta nacional, transfronteriza, reembolso y cambio de tipo impositivo.
2. Control de rechazo: Una factura emitida y después anulada no debe borrarse ni renumerarse silenciosamente.
3. Invariante: No aplicar nunca un tipo de IVA universal ni pretender garantizar la conformidad fiscal sin validación local.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
