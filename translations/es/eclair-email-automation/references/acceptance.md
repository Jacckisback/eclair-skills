# Plan de validación — Emails transaccionales

## Modelo de datos
Template, idioma, consentimiento, destinatario, dominio, evento, entrega.

## Implementación esperada
Preparar plantillas texto/HTML, DKIM/SPF/DMARC y entregabilidad; distinguir transaccional y marketing, registro sin secretos, baja de suscripción obligatoria.

## Tests que deben preverse
1. Nominal: Probar error SMTP, error de dirección, reintento y caducidad del token.
2. Control de rechazo: Un fallo SMTP no marca un email como entregado ni bloquea una cuenta definitivamente.
3. Invariante: No enviar un token de recuperación mediante una URL no verificada; nunca spam sin consentimiento.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
