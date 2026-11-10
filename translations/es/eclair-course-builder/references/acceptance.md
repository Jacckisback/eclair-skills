# Plan de validación — Creación de itinerarios

## Modelo de datos
Curso, módulo, lección, orden, borrador, versión publicada y autor.

## Implementación esperada
Establecer el esquema jerárquico; previsualizar antes de publicar; conservar los identificadores al reordenar; documentar el archivado.

## Tests que deben preverse
1. Nominal: Probar permutación de lecciones, despublicación y edición concurrente.
2. Control de rechazo: Cambiar el orden no reinicia el progreso de los estudiantes.
3. Invariante: Los borradores del formador no deben indexarse ni exponerse públicamente.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
