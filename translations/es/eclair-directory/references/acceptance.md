# Plan de validación — Directorio profesional

## Modelo de datos
Ficha, categoría, ubicación, contacto público, estado de verificación.

## Implementación esperada
Separar datos profesionales públicos y privados; crear páginas de categoría, canonical, moderación y filtros acotados.

## Tests que deben preverse
1. Nominal: Probar fichas falsas, duplicados, eliminación y búsqueda vacía.
2. Control de rechazo: Una ficha pendiente no aparece ni en el sitemap ni en los datos estructurados.
3. Invariante: No publicar dirección personal, teléfono ni datos de contacto sensibles sin autorización.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
