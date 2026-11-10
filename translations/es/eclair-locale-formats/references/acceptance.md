# Plan de validación — Formatos regionales

## Modelo de datos
Idioma, país, moneda, zona horaria.

## Implementación esperada
Centralizar el formateo en el servidor, no escribir nunca un formato fijo en el código de las plantillas.

## Tests que deben preverse
1. Nominal: Comparar una fecha y un precio en francés, inglés y alemán.
2. Control de rechazo: Una moneda desconocida no se muestra con un símbolo por defecto engañoso.
3. Invariante: Un precio mostrado corresponde siempre a la moneda realmente facturada.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
