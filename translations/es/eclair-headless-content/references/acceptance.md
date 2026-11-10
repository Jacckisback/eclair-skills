# Plan de validación — Contenido para aplicaciones e IA

## Modelo de datos
Versión Markdown, llms.txt, feeds, sitemap.

## Implementación esperada
Apoyarse en las salidas nativas legibles por máquina, documentar su formato y su actualidad para la aplicación cliente.

## Tests que deben preverse
1. Nominal: Leer una página en HTML y en Markdown y comparar.
2. Control de rechazo: Un borrador no tiene versión Markdown accesible.
3. Invariante: Ningún contenido privado se expone a través de estas salidas.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
