# Plan de validación — Paginación y listados

## Modelo de datos
Listado, página actual, tamaño de página, enlaces anterior y siguiente.

## Implementación esperada
Fijar un tamaño de página razonable, direcciones estables por página y enlaces accesibles.

## Tests que deben preverse
1. Nominal: Recorrer la primera página, una intermedia y la última.
2. Control de rechazo: Un número de página fuera de los límites responde con un error limpio, no con un listado vacío indexable.
3. Invariante: Los parámetros de página están acotados y validados.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
