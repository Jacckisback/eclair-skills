# Plan de validación — Promociones y cupones

## Modelo de datos
Código, presupuesto, fechas, cuota, condiciones del carrito, usos y exclusiones.

## Implementación esperada
Definir el orden de cálculo y el redondeo; verificar el cupón antes del pedido; descontar los usos de forma atómica; trazar la cancelación y la devolución.

## Tests que deben preverse
1. Nominal: Probar cupones caducados, agotados, umbral y exclusiones.
2. Control de rechazo: Dos pedidos simultáneos no pueden consumir el último cupón único.
3. Invariante: La decisión de elegibilidad procede de los datos del servidor y no del descuento introducido en HTML.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
