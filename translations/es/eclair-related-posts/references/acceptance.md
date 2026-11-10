# Plan de validación — Contenidos relacionados

## Modelo de datos
Contenido, categoría, palabras comunes, lista de enlaces calculada.

## Implementación esperada
Calcular las relaciones al publicar o mediante una tarea, renderizarlas con un bloque estático cacheable, limitar a unos pocos enlaces.

## Tests que deben preverse
1. Nominal: Comprobar los enlaces propuestos en varios artículos de categorías distintas.
2. Control de rechazo: Un artículo eliminado deja de proponerse tras la regeneración.
3. Invariante: Ninguna relación apunta a un contenido no publicado.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
