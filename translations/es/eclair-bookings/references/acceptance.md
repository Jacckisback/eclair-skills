# Plan de validación — Reservas de negocio

## Modelo de datos
Recurso, franja, capacidad, zona horaria, estado y reserva.

## Implementación esperada
Definir reglas de disponibilidad y cancelación, bloquear las franjas de forma transaccional, distinguir opción y reserva en firme.

## Tests que deben preverse
1. Nominal: Probar clientes simultáneos, cambios de hora y cancelación.
2. Control de rechazo: Última plaza reservada simultáneamente => una sola confirmación.
3. Invariante: Ningún calendario GET en caché sustituye a la validación transaccional de la disponibilidad.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
