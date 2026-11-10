# Plan de validación — Enlaces de pago

## Modelo de datos
Producto o variante, enlace de pago, proveedor.

## Implementación esperada
Crear el enlace en el proveedor, pegarlo en la ficha o en la variante, probar en modo de prueba, comprobar el recibo y el reembolso en el proveedor.

## Tests que deben preverse
1. Nominal: Comprar en modo de prueba y comprobar el importe y el recibo.
2. Control de rechazo: Un enlace a un dominio no reconocido es rechazado.
3. Invariante: Ningún dato bancario en el sitio; un enlace solo lleva al dominio del proveedor.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
