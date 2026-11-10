# Plan de validación — Índice automático

## Modelo de datos
Subtítulos, anclas, niveles.

## Implementación esperada
Generar el índice a partir de los subtítulos en el renderizado del servidor, con anclas estables y sin JavaScript obligatorio.

## Tests que deben preverse
1. Nominal: Comprobar el índice en un contenido con tres niveles de subtítulos.
2. Control de rechazo: Un contenido corto sin subtítulos no muestra ningún índice vacío.
3. Invariante: Las anclas generadas están escapadas y son únicas.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
