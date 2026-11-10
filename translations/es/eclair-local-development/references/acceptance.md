# Plan de validación — Desarrollo local

## Modelo de datos
Versión de PHP, servidor web, copia del sitio, datos de prueba.

## Implementación esperada
Instalar la misma versión de PHP y las mismas reglas de servidor, restaurar una copia de seguridad anonimizada, lanzar los tests.

## Tests que deben preverse
1. Nominal: Arrancar el sitio local y hacer pasar la suite de tests.
2. Control de rechazo: Una copia local no envía ningún correo electrónico real.
3. Invariante: Los datos reales de clientes no se copian en local sin anonimización.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
