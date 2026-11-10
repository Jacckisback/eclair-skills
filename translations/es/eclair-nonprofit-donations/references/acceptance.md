# Plan de validación — Donaciones y asociaciones

## Modelo de datos
Causa, proyecto, importe, enlace de donación, recibo.

## Implementación esperada
Presentar la misión y el uso de los fondos, vincular los botones de donación a enlaces del proveedor, remitir la gestión de los recibos al proveedor o a la asociación.

## Tests que deben preverse
1. Nominal: Hacer una donación en modo de prueba y seguir el recorrido completo.
2. Control de rechazo: Un importe modificado en la página no cambia el importe cobrado.
3. Invariante: Ninguna promesa de ventaja fiscal sin confirmación de la asociación.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
