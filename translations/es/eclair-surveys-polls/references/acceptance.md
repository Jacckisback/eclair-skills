# Plan de validación — Sondeos y encuestas

## Modelo de datos
Pregunta, opciones, respuesta, participante anónimo, resultados agregados.

## Implementación esperada
Definir el anonimato, la limitación de los votos múltiples, la visualización de los resultados agregados y la duración del sondeo.

## Tests que deben preverse
1. Nominal: Votar, consultar los resultados y cerrar el sondeo.
2. Control de rechazo: Un segundo voto del mismo participante se ignora.
3. Invariante: Ninguna respuesta individual se publica; solo resultados agregados.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
