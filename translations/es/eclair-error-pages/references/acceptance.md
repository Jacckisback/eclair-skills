# Plan de validación — Páginas de error

## Modelo de datos
Página de error, enlaces útiles, registro de las direcciones no encontradas.

## Implementación esperada
Componer una página 404 útil en el tema del sitio, proponer la página de inicio y las páginas clave, tratar los 404 frecuentes mediante redirección.

## Tests que deben preverse
1. Nominal: Solicitar una dirección inexistente y verificar el estado 404 y el contenido.
2. Control de rechazo: Una página no encontrada nunca responde con un estado 200.
3. Invariante: La página de error no muestra ninguna traza técnica.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
