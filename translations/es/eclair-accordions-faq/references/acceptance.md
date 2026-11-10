# Plan de validación — FAQ y acordeones

## Modelo de datos
Pregunta, respuesta, orden.

## Implementación esperada
Redactar preguntas reales de clientes, utilizar el bloque FAQ nativo, que genera también el marcado, limitar el número por página.

## Tests que deben preverse
1. Nominal: Comprobar la apertura con el teclado y el marcado generado.
2. Control de rechazo: Una FAQ vacía no emite ningún marcado.
3. Invariante: Ninguna respuesta inventada ni promesa sin verificar.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
