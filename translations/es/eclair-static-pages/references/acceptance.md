# Plan de validación — Páginas del sitio

## Modelo de datos
Página, dirección, bloques, página superior, estado, entrada de menú.

## Implementación esperada
Enumerar las páginas necesarias, fijar las direcciones antes de redactar, componer cada página en bloques y enlazar las páginas entre sí.

## Tests que deben preverse
1. Nominal: Crear la estructura en árbol completa y controlar cada dirección, el menú y las migas de pan.
2. Control de rechazo: Una página renombrada responde con una única redirección 301, nunca con un error 404.
3. Invariante: No cambiar nunca la dirección de una página publicada sin una redirección verificada.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
