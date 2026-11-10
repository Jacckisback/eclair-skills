# Plan de validación — Simuladores y calculadoras

## Modelo de datos
Parámetros, fórmula, resultado.

## Implementación esperada
Calcular en el navegador con una fórmula validada por el cliente, mostrar hipótesis y límites, proponer después la toma de contacto.

## Tests que deben preverse
1. Nominal: Comparar los resultados con un conjunto de casos calculados a mano.
2. Control de rechazo: Un valor absurdo o negativo muestra un mensaje, no un resultado falso.
3. Invariante: El resultado es orientativo y se anuncia como tal; ningún dato introducido se envía al servidor.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
