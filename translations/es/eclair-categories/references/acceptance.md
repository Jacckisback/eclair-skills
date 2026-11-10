# Plan de validación — Categorías

## Modelo de datos
Categoría, dirección, descripción, contenidos asociados.

## Implementación esperada
Definir pocas categorías estables, redactar su descripción, asociar cada contenido a una categoría principal.

## Tests que deben preverse
1. Nominal: Crear las categorías, asociar los contenidos y comprobar las páginas de categoría y su paginación.
2. Control de rechazo: Una categoría sin contenido publicado no se ofrece en la navegación.
3. Invariante: No crear categorías vacías o duplicadas que diluyan el sitio.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
