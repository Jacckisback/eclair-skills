# Plan de validación — Arquitectura Commerce Pro

## Modelo de datos
Catálogo, carrito, precios fijados por línea, pedido, pago, reembolso, stock, factura y registro de estados.

## Implementación esperada
Diseñar una máquina de estados pedido/payment, separar la lectura pública de las escrituras privadas, elegir un almacenamiento transaccional, formalizar el conector PSP; identificar los puntos que Éclair v2 no proporciona.

## Tests que deben preverse
1. Nominal: Simular compra, confirmación por webhook, reintento, reembolso, stock y cancelación.
2. Control de rechazo: Una misma notificación de pago entregada dos veces => una sola transición de pedido.
3. Invariante: Ningún pago se declara correcto a partir de la sola redirección del navegador; el servidor valida un evento PSP autenticado.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
