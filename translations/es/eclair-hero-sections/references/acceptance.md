# Plan de validación — Secciones de cabecera

## Modelo de datos
Título, subtítulo, imagen, botón.

## Implementación esperada
Escribir una promesa precisa, elegir una imagen ligera, mantener un único título principal y un botón.

## Tests que deben preverse
1. Nominal: Medir la visualización del elemento más grande en móvil.
2. Control de rechazo: Sin imagen, la sección sigue siendo legible y con contraste.
3. Invariante: La imagen principal tiene dimensiones explícitas y no retrasa la visualización.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
