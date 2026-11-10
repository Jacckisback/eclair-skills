# Plan de validación — Flujo editorial

## Modelo de datos
Borrador, autor, revisor, fecha prevista, estado, entrada de planificación.

## Implementación esperada
Fijar quién redacta y quién publica según los permisos nativos, utilizar la planificación editorial y los borradores, mantener una revisión humana antes de cualquier puesta en línea.

## Tests que deben preverse
1. Nominal: Hacer pasar un contenido de la idea al borrador y después a la publicación por una persona habilitada.
2. Control de rechazo: Una cuenta limitada a los contenidos no puede ni cambiar los ajustes ni publicar en lugar de otro rol.
3. Invariante: Un agente o un redactor sin permiso de publicación no pone nada en línea.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
