# Plan de validación — Búsqueda en el sitio

## Modelo de datos
Índice de los contenidos publicados, título, extracto, dirección.

## Implementación esperada
Generar un índice estático de los contenidos públicos mediante una tarea programada, servirlo en GET cacheable y buscar en el navegador con una página alternativa sin JavaScript.

## Tests que deben preverse
1. Nominal: Buscar un término presente, uno ausente y uno acentuado, y comprobar el tiempo de respuesta.
2. Control de rechazo: Un borrador o una página privada nunca aparece en el índice.
3. Invariante: El índice solo contiene contenidos públicos; ninguna consulta de un visitante se registra junto con su identidad.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
