# Plan de validación — Respuesta a incidentes

## Modelo de datos
Incidente, cronología, cuentas afectadas, copia de seguridad sana.

## Implementación esperada
Aislar, conservar las pruebas, cambiar los secretos, comprobar la integridad, restaurar una copia de seguridad sana, informar a las personas afectadas si es necesario.

## Tests que deben preverse
1. Nominal: Realizar el ejercicio sobre una copia: detección, restauración, control.
2. Control de rechazo: Un sitio restaurado no vuelve a ponerse en línea antes de cambiar todos los secretos.
3. Invariante: No eliminar nunca los rastros antes de haberlos copiado.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
