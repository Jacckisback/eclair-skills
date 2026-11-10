# Plan de validación — Fuentes

## Modelo de datos
Fuente, grosores, archivo autoalojado, alternativa del sistema.

## Implementación esperada
Utilizar las fuentes del sistema o la fuente de títulos autoalojada de las direcciones artísticas, limitar los grosores.

## Tests que deben preverse
1. Nominal: Verificar la ausencia de peticiones a terceros y de saltos de texto.
2. Control de rechazo: Una fuente no disponible deja una alternativa legible.
3. Invariante: Ninguna fuente se carga desde un servicio de terceros.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
