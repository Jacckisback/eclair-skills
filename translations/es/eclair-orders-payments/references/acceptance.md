# Plan de validación — Pedidos y pagos

## Modelo de datos
Pedido, intento de pago, identificador del proveedor, prueba del webhook, idempotency key, reembolso.

## Implementación esperada
Detallar las transiciones autorizadas; almacenar la prueba de la notificación y su marca de tiempo; procesar el webhook de forma duradera; prever reconciliation y reembolso parcial.

## Tests que deben preverse
1. Nominal: Probar webhook invertido, fuera de orden, reenviado y pago rechazado.
2. Control de rechazo: Un webhook sin firma válida no modifica ni el pedido ni el acceso LMS.
3. Invariante: No almacenar nunca datos de tarjeta bancaria en bruto; checkout alojado en el proveedor y firma de los webhooks verificada.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
