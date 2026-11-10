# Plan de validación — Anuncios clasificados

## Modelo de datos
Anuncio, anunciante, categoría, estado, denuncia.

## Implementación esperada
Definir envío, moderación, vigencia, denuncia y puesta en contacto sin exponer los datos de contacto.

## Tests que deben preverse
1. Nominal: Simular envío, moderación, caducidad y denuncia.
2. Control de rechazo: Un anuncio rechazado o caducado deja de ser accesible.
3. Invariante: Ningún anuncio publicado sin moderación; datos de contacto nunca mostrados en claro.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
