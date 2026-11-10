# Plan de validación — Conectores API

## Modelo de datos
OAuth/token, scopes, cuotas, errores, paginación, versión y registros.

## Implementación esperada
Definir el esquema de la API, aislar los secretos, validar los esquemas entrantes, prever timeouts/circuit breaker y versionado.

## Tests que deben preverse
1. Nominal: Probar timeout, 429, 500, respuesta mal formada y revocación.
2. Control de rechazo: Un 500 del proveedor no daña los datos locales ni la presentación pública.
3. Invariante: No permitir SSRF ni URL dinámicas arbitrarias; no registrar nunca un token.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
