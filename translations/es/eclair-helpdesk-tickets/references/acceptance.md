# Plan de validación — Asistencia y tickets

## Modelo de datos
Ticket, solicitante, estado, intercambios, prioridad.

## Implementación esperada
Empezar con formulario de contacto y bandeja de entrada; diseñar estados, plazos y área de seguimiento para más adelante.

## Tests que deben preverse
1. Nominal: Recorrer una solicitud desde la apertura hasta el cierre.
2. Control de rechazo: Un ticket no puede leerse adivinando su número.
3. Invariante: Un solicitante solo ve sus propios tickets.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
