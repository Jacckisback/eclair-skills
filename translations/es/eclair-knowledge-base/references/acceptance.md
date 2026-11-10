# Plan de validación — Base de conocimientos

## Modelo de datos
Artículo de ayuda, sección, versión, fecha de actualización.

## Implementación esperada
Organizar por problemas de los usuarios, una respuesta por página, navegación por secciones y búsqueda interna.

## Tests que deben preverse
1. Nominal: Resolver tres problemas tipo únicamente con la documentación.
2. Control de rechazo: Un artículo obsoleto se fecha y se señala, no se deja como válido.
3. Invariante: Ningún procedimiento no probado se publica.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
