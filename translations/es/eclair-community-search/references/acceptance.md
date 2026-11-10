# Plan de validación — Búsqueda en el foro

## Modelo de datos
Término, índice acotado, idioma, categoría, página, estado y permisos.

## Implementación esperada
Normalizar el texto, indexar las publicaciones autorizadas, paginar y limitar el coste, retirar del resultado los objetos eliminados.

## Tests que deben preverse
1. Nominal: Probar frase vacía, inyección, búsqueda masiva, temas privados.
2. Control de rechazo: Un visitante no debe ver el extracto de un debate privado en una sugerencia.
3. Invariante: El filtrado de permisos se aplica en cada búsqueda, no solo en el momento de la indexación.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
