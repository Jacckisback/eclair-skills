# Plan de validación — Tareas programadas

## Modelo de datos
Tarea, frecuencia, última ejecución, resultado.

## Implementación esperada
Declarar la tarea en el manifiesto (como máximo una vez por hora), llamar a la dirección secreta del núcleo desde el planificador del proveedor de alojamiento, registrar.

## Tests que deben preverse
1. Nominal: Ejecutar la tarea dos veces seguidas y verificar un solo efecto.
2. Control de rechazo: Una llamada sin el token secreto no desencadena nada.
3. Invariante: La dirección secreta de las tareas nunca se publica; cada tarea es idempotente.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
