# Plan de validación — Idiomas de derecha a izquierda

## Modelo de datos
Dirección del texto, propiedades lógicas CSS, iconos orientados.

## Implementación esperada
Utilizar las propiedades lógicas CSS en el tema de sitio, probar cada plantilla en dir=rtl.

## Tests que deben preverse
1. Nominal: Mostrar las páginas tipo de derecha a izquierda sin desbordamiento.
2. Control de rechazo: Una mezcla de idiomas no rompe el orden de lectura.
3. Invariante: Ningún texto de usuario se inyecta sin escapado, incluidos los caracteres de dirección.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
