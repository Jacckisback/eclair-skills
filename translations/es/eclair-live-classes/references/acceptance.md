# Plan de validación — Clases en directo

## Modelo de datos
Sesión, fecha, zona horaria, enlace de conexión, inscritos.

## Implementación esperada
Publicar el calendario de sesiones en GET, enviar el enlace de conexión a través del servicio de videoconferencia o por correo electrónico, no en una página pública.

## Tests que deben preverse
1. Nominal: Verificar la visualización de las fechas en dos zonas horarias.
2. Control de rechazo: Una sesión pasada deja de ofrecerse para inscripción.
3. Invariante: El enlace de una sesión de pago o privada nunca se publica.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
