# Plan de validación — Contenidos multilingües

## Modelo de datos
Contenido, idioma, versión vinculada, dirección por idioma.

## Implementación esperada
Comprobar en las capacidades los idiomas admitidos por el sitio, organizar una estructura en árbol por idioma, enlazar las versiones y controlar hreflang.

## Tests que deben preverse
1. Nominal: Crear una página en dos idiomas y comprobar los enlaces cruzados y hreflang.
2. Control de rechazo: Un idioma sin traducción no remite a una página vacía.
3. Invariante: Ninguna traducción automática se publica sin revisión humana.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
