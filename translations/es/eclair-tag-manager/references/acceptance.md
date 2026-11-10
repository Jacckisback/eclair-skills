# Plan de validación — Gestor de etiquetas

## Modelo de datos
Contenedor, etiquetas, activadores, consentimiento.

## Implementación esperada
Enumerar las etiquetas realmente necesarias, buscar una alternativa en el servidor, documentar el bloqueo por la política de contenido nativa.

## Tests que deben preverse
1. Nominal: Elaborar el inventario de las etiquetas y su alternativa.
2. Control de rechazo: Una etiqueta no justificada no se añade.
3. Invariante: Ningún contenedor que permita inyectar código arbitrario sin revisión.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
