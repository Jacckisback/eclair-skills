# Plan de validación — Cabeceras de seguridad

## Modelo de datos
Cabeceras HTTP, Content-Security-Policy, HTTPS.

## Implementación esperada
Anotar las cabeceras servidas, verificar HTTPS en todas partes, probar las reglas del servidor web suministradas con el núcleo.

## Tests que deben preverse
1. Nominal: Analizar las cabeceras de una página pública y de la administración.
2. Control de rechazo: Un archivo sensible o de datos nunca es servido por el servidor web.
3. Invariante: Ninguna cabecera de protección se retira ni se relaja.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
