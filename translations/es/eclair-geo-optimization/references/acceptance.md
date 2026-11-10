# Plan de validación — GEO y agentes de IA

## Modelo de datos
Contenido verificable, procedencia, semántica, llms.txt, Markdown, Schema.org.

## Implementación esperada
Auditar la estructura, las respuestas factuales, las fuentes y la coherencia del Markdown; controlar los robots de IA sin prometer de más.

## Tests que deben preverse
1. Nominal: Probar la versión Markdown, las citas estructuradas y robots.txt.
2. Control de rechazo: Los hechos mostrados a robots y a humanos se mantienen coherentes y actualizados.
3. Invariante: No confundir puntuación GEO interna, citabilidad y posición garantizada.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
