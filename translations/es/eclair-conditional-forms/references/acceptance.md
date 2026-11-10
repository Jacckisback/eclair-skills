# Plan de validación — Formularios condicionales

## Modelo de datos
Campo, condición, rama, validación.

## Implementación esperada
Describir las reglas como datos, aplicarlas en el servidor y en el navegador, probar cada rama.

## Tests que deben preverse
1. Nominal: Recorrer cada rama hasta el envío.
2. Control de rechazo: Un campo obligatorio de una rama activa no se puede eludir.
3. Invariante: La validación del servidor nunca confía en los campos ocultos en el navegador.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
