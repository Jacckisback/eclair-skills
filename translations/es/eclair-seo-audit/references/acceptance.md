# Plan de validación — Auditoría SEO técnica

## Modelo de datos
URLs, canonicals, sitemap, redirecciones, títulos, estados HTTP, datos estructurados.

## Implementación esperada
Rastrear las páginas autorizadas, anotar las divergencias, priorizar las causas estructurales, comprobar la cobertura y el plan de corrección.

## Tests que deben preverse
1. Nominal: Probar barra final, acentos, paginaciones, 404, sitemap y robots.
2. Control de rechazo: Ninguna URL crítica queda huérfana o redirigida en cadena tras la actualización.
3. Invariante: No prometer posiciones; no modificar las URLs existentes sin un plan de redirects.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
