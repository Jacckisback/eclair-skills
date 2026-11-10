# Plan de validación — Medición de ventas

## Modelo de datos
Embudo, pedidos confirmados, reembolsos, tasa de conversión, ingresos netos, consentimientos.

## Implementación esperada
Definir eventos y métricas sin reutilizar datos sensibles; conciliar los totales de pedidos, facturas rectificativas y pagos; prever una síntesis agregada.

## Tests que deben preverse
1. Nominal: Probar los ingresos tras un reembolso y la interrupción del recuento.
2. Control de rechazo: La agregación no debe contar dos veces el mismo pago ni divulgar un pedido identificable.
3. Invariante: Los datos analíticos personales exigen una base legal y no deben filtrarse a través de la caché.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
