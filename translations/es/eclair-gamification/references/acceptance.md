# Plan de validación — Insignias y puntos

## Modelo de datos
Regla, puntos, insignia, clasificación.

## Implementación esperada
Fijar reglas sencillas y verificables en el servidor, prever la retirada en caso de abuso y la opción de no aparecer en la clasificación.

## Tests que deben preverse
1. Nominal: Simular obtención, retirada y visualización de la clasificación.
2. Control de rechazo: Una acción repetida artificialmente no otorga puntos por duplicado.
3. Invariante: Ningún punto se concede basándose en una información enviada por el navegador.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
