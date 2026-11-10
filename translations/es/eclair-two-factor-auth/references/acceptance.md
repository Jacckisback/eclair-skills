# Plan de validación — Autenticación en dos pasos

## Modelo de datos
Cuenta, secreto TOTP, códigos de respaldo.

## Implementación esperada
Hacer que cada persona active la autenticación en dos pasos, guardar los códigos de respaldo, prever la pérdida del dispositivo.

## Tests que deben preverse
1. Nominal: Activar, cerrar sesión, volver a iniciar sesión con el segundo factor.
2. Control de rechazo: Una contraseña correcta sin segundo factor no da acceso.
3. Invariante: Los secretos y los códigos de respaldo nunca se copian en un chat, un correo electrónico o un repositorio.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
