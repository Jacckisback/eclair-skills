# Plan de validación — Comentarios

## Modelo de datos
Comentario, autor, estado de moderación, artículo, fecha.

## Implementación esperada
Definir cola de moderación, reglas antispam, avisos legales y visualización en caché; proponer mientras tanto un servicio externo o una vía de contacto.

## Tests que deben preverse
1. Nominal: Simular el envío, la moderación, la publicación y la eliminación de un comentario.
2. Control de rechazo: Un comentario pendiente o rechazado nunca aparece en una página en caché.
3. Invariante: Ningún comentario se muestra sin moderación; ninguna dirección de correo electrónico se hace pública.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
