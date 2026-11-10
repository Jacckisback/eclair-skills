# Plan de validación — Pestañas

## Modelo de datos
Pestaña, título, panel.

## Implementación esperada
Construir un bloque de pestañas con roles ARIA, navegación con las flechas y alternativa en secciones apiladas.

## Tests que deben preverse
1. Nominal: Recorrer las pestañas con el teclado y con lector de pantalla.
2. Control de rechazo: Sin JavaScript, todos los paneles son visibles.
3. Invariante: Todo el contenido permanece en el HTML y, por tanto, es legible sin JavaScript.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
