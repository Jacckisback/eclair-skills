# Plan de validación — Notificaciones de comunidad

## Modelo de datos
Suscripción, mención, notificación, canal, preferencia, estado.

## Implementación esperada
Emitir eventos tras una escritura validada, filtrar por permisos en el momento de la lectura y del envío, aplicar la baja de suscripción.

## Tests que deben preverse
1. Nominal: Probar notificaciones repetidas, baja de suscripción y retirada de permiso.
2. Control de rechazo: Tras la revocación del acceso, ninguna notificación nueva contiene un extracto privado.
3. Invariante: No revelar nunca contenido de categorías privadas en email, push o digest.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
