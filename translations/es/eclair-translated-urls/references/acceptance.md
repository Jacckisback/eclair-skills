# Plan de validación — Direcciones traducidas

## Modelo de datos
Dirección por idioma, redirecciones, canonical, hreflang.

## Implementación esperada
Fijar una convención de direcciones por idioma, traducir los slugs antes de publicar, comprobar canonical y hreflang generados por el núcleo.

## Tests que deben preverse
1. Nominal: Comprobar canonical y hreflang de cada versión.
2. Control de rechazo: Dos idiomas nunca comparten la misma dirección.
3. Invariante: Ninguna dirección publicada se cambia sin redirección.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
