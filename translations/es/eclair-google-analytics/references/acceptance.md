# Plan de validación — Google Analytics

## Modelo de datos
Identificador de medición, consentimiento, eventos.

## Implementación esperada
Verificar primero si basta una medición sin cookies; si no, consentimiento previo, y constatación de que la política de contenido nativa no está abierta a las extensiones.

## Tests que deben preverse
1. Nominal: Verificar la ausencia de peticiones antes del consentimiento.
2. Control de rechazo: Tras un rechazo, no se envía ningún dato.
3. Invariante: Ningún script de medición cargado antes del consentimiento ni eludiendo la Content-Security-Policy.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
