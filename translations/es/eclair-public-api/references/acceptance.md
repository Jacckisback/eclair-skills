# Plan de validación — API pública de solo lectura

## Modelo de datos
Recurso, campos públicos, paginación, versión.

## Implementación esperada
Declarar rutas GET cacheables que devuelvan JSON acotado y versionado; documentar que la escritura no está abierta.

## Tests que deben preverse
1. Nominal: Leer lista y detalle, paginación y caso vacío.
2. Control de rechazo: Un contenido no publicado no es devuelto por ninguna ruta.
3. Invariante: Solo se exponen contenidos ya públicos; ningún identificador interno sensible.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
