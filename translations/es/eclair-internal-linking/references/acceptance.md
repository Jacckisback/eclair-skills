# Plan de validación — Enlazado interno

## Modelo de datos
Página de origen, página de destino, texto de anclaje, páginas huérfanas.

## Implementación esperada
Cartografiar los enlaces, localizar las páginas huérfanas, añadir enlaces útiles con textos de anclaje descriptivos.

## Tests que deben preverse
1. Nominal: Comprobar que cada página importante recibe al menos un enlace interno.
2. Control de rechazo: Ningún enlace interno apunta a una redirección o a un error.
3. Invariante: Ningún enlace se añade automáticamente sin revisar el contexto.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
