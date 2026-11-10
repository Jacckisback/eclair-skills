# Plan de validación — Revista y actualidad

## Modelo de datos
Artículo, sección, autor, portada, fecha.

## Implementación esperada
Estructurar secciones y portada, cuidar autores y fechas, utilizar las funciones nativas para los medios (imágenes grandes, planificación, feeds).

## Tests que deben preverse
1. Nominal: Publicar una portada de prueba y verificar secciones, feeds y sitemap.
2. Control de rechazo: Un artículo corregido muestra su fecha de actualización.
3. Invariante: Ninguna información sin fuente presentada como un hecho.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
