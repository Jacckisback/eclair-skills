# Plan de validación — Accesibilidad WCAG

## Modelo de datos
Estructura de los títulos, navegación con teclado, foco, formularios, medios, contrastes.

## Implementación esperada
Realizar una auditoría con teclado y lector de pantalla, comprobar axe-core, los contrastes, los mensajes de error y el movimiento reducido.

## Tests que deben preverse
1. Nominal: Probar recorridos sin ratón, errores de formulario y zoom al 200 %.
2. Control de rechazo: Un formulario sigue siendo comprensible sin color y desde el teclado.
3. Invariante: No eliminar el foco visible ni hacer que una funcionalidad dependa únicamente del color o de un gesto.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
