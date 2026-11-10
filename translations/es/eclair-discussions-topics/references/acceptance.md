# Plan de validación — Temas y respuestas

## Modelo de datos
Tema, respuesta, versión, autor, marca de tiempo, fijado, cerrado, eliminado.

## Implementación esperada
Definir jerarquía de respuestas, paginación, historial de ediciones, menciones y enlaces permanentes; tratar envíos idempotentes.

## Tests que deben preverse
1. Nominal: Probar respuestas concurrentes, mensaje borrado y tema cerrado.
2. Control de rechazo: Un miembro no puede editar ni eliminar la respuesta de otro sin permiso explícito.
3. Invariante: Escapar Markdown/HTML y verificar el permiso de edición en cada publicación.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
