# Plan de validación — Preproducción y puesta en línea

## Modelo de datos
Copia de prueba, diferencias, lista de comprobación de puesta en línea.

## Implementación esperada
Restaurar una copia de seguridad en un subdominio protegido y no indexable, validar en él el tema y las extensiones, y después reproducir en producción.

## Tests que deben preverse
1. Nominal: Recorrer un cambio de tema desde la copia hasta la producción.
2. Control de rechazo: La copia de prueba no está indexada ni es accesible sin autenticación.
3. Invariante: La copia de prueba está protegida con contraseña y bloqueada para los robots.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
