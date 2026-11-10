# Plan de validación — Migración de WordPress

## Modelo de datos
Exportación de WordPress, IDs antiguos, slugs, medios, categorías, autores, redirecciones y consultas ?p=.

## Implementación esperada
Utilizar la funcionalidad nativa WordPress; inventariar las URLs históricas, simular la importación, comparar slug/canonical, conservar los enlaces exactos y los medios, proporcionar un plan de rollback.

## Tests que deben preverse
1. Nominal: Probar URL con barra final, query alias, acentos, imágenes y páginas eliminadas.
2. Control de rechazo: Para cada URL antigua indexada, obtener un 200 exacto o una redirección 301 específica.
3. Invariante: Evitar los 404 y las eliminaciones de URLs; nunca un cambio de DNS sin pruebas ni copias de seguridad.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
