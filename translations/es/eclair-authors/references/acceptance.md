# Plan de validación — Autores y firmas

## Modelo de datos
Autor, biografía, cargo, enlaces, contenidos firmados.

## Implementación esperada
Completar los perfiles reales, vincular cada artículo a su autor, comprobar la página de autor y los datos estructurados generados por el núcleo.

## Tests que deben preverse
1. Nominal: Rellenar un perfil y comprobar la firma, la página de autor y el marcado.
2. Control de rechazo: Una cuenta desactivada o sin contenido publicado no expone ninguna página de autor.
3. Invariante: No inventar nunca un autor, un título académico o una experiencia.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
