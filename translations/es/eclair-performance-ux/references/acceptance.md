# Plan de validación — Rendimiento UX

## Modelo de datos
LCP, CLS, INP, peso de los assets, CSS, JS, caché y fuentes.

## Implementación esperada
Medir antes/después mediante tools/measure.php --check, Chrome Lighthouse y red lenta, optimizar imágenes y scripts.

## Tests que deben preverse
1. Nominal: Probar el sitio público sin extensión, con extensión y en móvil.
2. Control de rechazo: Toda mejora declarada va acompañada de mediciones reproducibles antes/después.
3. Invariante: No degradar la ruta de caché PHP ni desactivar la CSP por comodidad.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
