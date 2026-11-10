# Plan de validación — Suscripción a la newsletter

## Modelo de datos
Dirección de correo electrónico, consentimiento, fecha, origen.

## Implementación esperada
Utilizar una página de suscripción alojada por el servicio de e-mailing o un enlace, mientras el sitio no pueda recibir suscripciones por sí mismo; doble confirmación.

## Tests que deben preverse
1. Nominal: Suscribirse, confirmar, darse de baja.
2. Control de rechazo: Una suscripción no confirmada no recibe ningún envío.
3. Invariante: Ninguna dirección se añade a una lista sin consentimiento explícito y prueba.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
