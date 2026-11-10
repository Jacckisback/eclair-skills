# Plan de validación — Campos personalizados

## Modelo de datos
Campo, tipo declarado, valor validado, bloque o ajuste que lo contiene.

## Implementación esperada
Declarar los campos en el manifiesto (tipos admitidos por el núcleo), dejar que el núcleo valide y almacene, renderizar con escapado.

## Tests que deben preverse
1. Nominal: Declarar un bloque con campos de texto, número y selección, y comprobar después la validación y el renderizado.
2. Control de rechazo: Un valor fuera de formato es rechazado por el núcleo y nunca llega al renderizado.
3. Invariante: Todo valor mostrado pasa por e(); ningún campo contiene secretos.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
