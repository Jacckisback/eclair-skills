# Plan de validación — Desbloqueo progresivo

## Modelo de datos
Lección, regla de desbloqueo, fecha o condición, inscrito.

## Implementación esperada
Describir las reglas (fecha, plazo tras la inscripción, lección anterior), aplicarlas en el servidor en cada solicitud.

## Tests que deben preverse
1. Nominal: Simular el paso del tiempo y la validación de una lección.
2. Control de rechazo: Una dirección de lección bloqueada adivinada no devuelve su contenido.
3. Invariante: Una lección bloqueada nunca se envía al navegador, ni siquiera oculta.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
