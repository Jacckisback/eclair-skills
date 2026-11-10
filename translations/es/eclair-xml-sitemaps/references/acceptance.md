# Plan de validación — Sitemap XML

## Modelo de datos
Entradas de sitemap, fechas, imágenes, idiomas.

## Implementación esperada
Controlar el sitemap generado por el núcleo, declararlo en las herramientas de los buscadores, vigilar los errores de cobertura.

## Tests que deben preverse
1. Nominal: Validar el sitemap y compararlo con el número de páginas publicadas.
2. Control de rechazo: Una página en borrador o redirigida no figura en él.
3. Invariante: El sitemap solo enumera páginas publicadas e indexables.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
