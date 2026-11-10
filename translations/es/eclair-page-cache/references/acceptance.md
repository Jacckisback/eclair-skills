# Plan de validación — Caché de páginas

## Modelo de datos
Página en caché, invalidación, variantes prohibidas.

## Implementación esperada
Medir la respuesta en caché, detectar lo que impide el almacenamiento en caché de una ruta de extensión, verificar la invalidación al modificar.

## Tests que deben preverse
1. Nominal: Medir el tiempo de respuesta antes y después de una modificación.
2. Control de rechazo: Una ruta de extensión declarada no cacheable nunca se sirve desde la caché.
3. Invariante: Ninguna página que contenga datos de sesión o personales entra en la caché compartida.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
