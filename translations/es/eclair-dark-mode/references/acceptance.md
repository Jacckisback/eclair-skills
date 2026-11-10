# Plan de validación — Modo oscuro

## Modelo de datos
Juegos de colores claro y oscuro, preferencia del visitante.

## Implementación esperada
Definir las variables de color del tema para prefers-color-scheme, comprobar contrastes, imágenes y logotipos.

## Tests que deben preverse
1. Nominal: Controlar los contrastes de los dos modos en las páginas tipo.
2. Control de rechazo: Un logotipo oscuro no se vuelve invisible en modo oscuro.
3. Invariante: No se necesita ninguna cookie para respetar la preferencia del sistema.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
