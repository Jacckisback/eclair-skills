# Plan de validación — Tablas de precios

## Modelo de datos
Oferta, precio, periodo, características, botón.

## Implementación esperada
Componer las ofertas en tarjetas comparables, mostrar los precios con o sin impuestos incluidos sin ambigüedad y vincular cada botón a la acción correcta.

## Tests que deben preverse
1. Nominal: Comparar tres ofertas en móvil y comprobar cada enlace.
2. Control de rechazo: Una oferta sin precio validado no se muestra.
3. Invariante: Ningún precio, descuento o mención legal inventados.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
