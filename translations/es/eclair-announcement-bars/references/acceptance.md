# Plan de validación — Barras de anuncio

## Modelo de datos
Mensaje, enlace, fechas de inicio y de fin.

## Implementación esperada
Renderizar la barra en el servidor con fechas de validez, sin desplazamiento del diseño, retirada automáticamente al vencimiento.

## Tests que deben preverse
1. Nominal: Mostrar, cerrar y dejar caducar una barra.
2. Control de rechazo: Después de la fecha de fin, la barra ya no aparece en ninguna página.
3. Invariante: Ningún anuncio caducado sigue siendo servido por la caché.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
