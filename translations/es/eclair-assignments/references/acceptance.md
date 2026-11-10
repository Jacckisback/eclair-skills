# Plan de validación — Tareas y correcciones

## Modelo de datos
Tarea, entrega, nota, comentario, alumno.

## Implementación esperada
Definir entrega, plazos, corrección y devolución; aislar cada trabajo para su autor y el corrector.

## Tests que deben preverse
1. Nominal: Simular entrega, corrección y consulta de la nota.
2. Control de rechazo: Un alumno no puede acceder al trabajo de otro.
3. Invariante: Un trabajo solo es legible por su autor y los correctores designados.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
