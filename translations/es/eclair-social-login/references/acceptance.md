# Plan de validación — Inicio de sesión con cuenta de terceros

## Modelo de datos
Proveedor de identidad, cuenta vinculada, consentimiento.

## Implementación esperada
Depende primero de las cuentas de miembro; diseñar el flujo OAuth con estado, PKCE y vinculación de cuenta explícita.

## Tests que deben preverse
1. Nominal: Simular inicio de sesión, vinculación y desvinculación.
2. Control de rechazo: Una respuesta OAuth repetida o falsificada se rechaza.
3. Invariante: Ninguna cuenta se fusiona basándose únicamente en una dirección de correo electrónico no verificada.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
