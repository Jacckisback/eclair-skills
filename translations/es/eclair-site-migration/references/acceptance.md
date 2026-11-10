# Plan de validación — Cambio de alojamiento o de dominio

## Modelo de datos
Copia de seguridad, nuevo alojamiento, DNS, redirecciones de dominio.

## Implementación esperada
Hacer una copia de seguridad, restaurar en el nuevo proveedor de alojamiento, verificar, cambiar el DNS, redirigir el dominio antiguo página a página.

## Tests que deben preverse
1. Nominal: Ensayar el traslado en un dominio de prueba.
2. Control de rechazo: Ninguna dirección antigua responde con un 404 tras el cambio.
3. Invariante: Los secretos del sitio nunca viajan por correo electrónico ni por mensajería.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
