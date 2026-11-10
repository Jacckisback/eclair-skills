# Plan de validación — Productos digitales

## Modelo de datos
Producto digital, compra, enlace de entrega temporal.

## Implementación esperada
Hacer que el archivo lo entregue el proveedor o un enlace firmado de duración limitada; no colocar nunca el archivo en una dirección pública.

## Tests que deben preverse
1. Nominal: Simular compra, entrega y caducidad del enlace.
2. Control de rechazo: Un enlace caducado o compartido deja de dar acceso al archivo.
3. Invariante: Ningún archivo de pago es accesible sin una compra verificada.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
