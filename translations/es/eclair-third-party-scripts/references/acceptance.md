# Plan de validación — Scripts de terceros

## Modelo de datos
Script, finalidad, peso, dominio, consentimiento requerido.

## Implementación esperada
Inventariar cada solicitud de script, buscar una alternativa sin script, documentar el bloqueo por la política de contenido nativa cuando exista.

## Tests que deben preverse
1. Nominal: Medir peso y peticiones antes y después de cada añadido aceptado.
2. Control de rechazo: Un script de un dominio no autorizado no se ejecuta.
3. Invariante: Ningún script se inyecta eludiendo la Content-Security-Policy.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
