# Plan de validación — Ofertas y códigos promocionales

## Modelo de datos
Oferta, comercio, código, fecha de fin, enlace.

## Implementación esperada
Mostrar condiciones y fecha de fin, retirar automáticamente las ofertas caducadas, marcar los enlaces de afiliación.

## Tests que deben preverse
1. Nominal: Publicar una oferta con fecha y comprobar su retirada al vencimiento.
2. Control de rechazo: Un enlace remunerado nunca aparece sin mención.
3. Invariante: Ninguna oferta caducada o no verificable presentada como válida.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
