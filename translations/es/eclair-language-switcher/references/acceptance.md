# Plan de validación — Selector de idioma

## Modelo de datos
Idioma actual, versiones disponibles, etiquetas.

## Implementación esperada
Enumerar los idiomas por su nombre en su propio idioma, apuntar a la versión equivalente, sin redirección automática forzada.

## Tests que deben preverse
1. Nominal: Cambiar de idioma desde una página profunda y llegar a su equivalente.
2. Control de rechazo: Si no hay equivalente, el enlace lleva a la página de inicio del idioma, no a un error.
3. Invariante: Ninguna redirección por dirección IP; se respeta la elección del visitante.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
