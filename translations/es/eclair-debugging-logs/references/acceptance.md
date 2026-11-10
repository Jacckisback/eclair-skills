# Plan de validación — Diagnóstico y registros

## Modelo de datos
Síntoma, registro del servidor, registro del sitio, hipótesis, corrección.

## Implementación esperada
Reproducir, leer los registros del servidor y del sitio, aislar la extensión causante desactivándola, corregir y después verificar.

## Tests que deben preverse
1. Nominal: Provocar un error en una extensión de prueba y localizarlo.
2. Control de rechazo: Ninguna traza técnica aparece en una página pública.
3. Invariante: La visualización de errores nunca se activa en el sitio público.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
