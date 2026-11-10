# Plan de validación — Artículos de blog

## Modelo de datos
Artículo, extracto, imagen principal, categoría, autor, fecha, estado de borrador o publicado.

## Implementación esperada
Crear los artículos como borrador desde la administración o el conector MCP, comprobar título, extracto, imagen y categoría, y dejar que una persona publique.

## Tests que deben preverse
1. Nominal: Crear un borrador completo, hacer que se publique y comprobar después su renderizado, el feed RSS y el sitemap.
2. Control de rechazo: Un borrador no aparece ni en el sitio público, ni en el sitemap, ni en el feed.
3. Invariante: No publicar ni eliminar nunca un contenido en lugar de la persona autorizada.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
