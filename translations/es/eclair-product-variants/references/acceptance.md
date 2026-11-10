# Plan de validación — Variantes y atributos

## Modelo de datos
Producto principal, variantes con SKU único, combinaciones de atributos, precio/stock propios, medio y estado.

## Implementación esperada
Definir el número máximo de combinaciones; garantizar la unicidad del SKU; proyectar las variantes en el renderizado GET; preparar una selección validada en el servidor durante el checkout.

## Tests que deben preverse
1. Nominal: Probar variantes ausentes, agotadas y desactivadas.
2. Control de rechazo: Dos combinaciones crean el mismo SKU => rechazo explícito antes de la publicación.
3. Invariante: No aceptar nunca como datos fiables un precio, un peso o un stock enviados por el navegador.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
