# Plan de validación — Conector MCP

## Modelo de datos
Cliente autorizado, token, herramientas disponibles, borradores creados.

## Implementación esperada
Hacer que el propietario active el conector, autorizar el cliente, trabajar con borradores y propuestas, saber cortar el acceso.

## Tests que deben preverse
1. Nominal: Crear un borrador mediante el conector y después revocar el acceso.
2. Control de rechazo: Tras la revocación, toda petición del cliente se rechaza.
3. Invariante: El conector no publica ni elimina; el acceso es revocable en cualquier momento.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
