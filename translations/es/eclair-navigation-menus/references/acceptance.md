# Plan de validación — Menús de navegación

## Modelo de datos
Menú, entrada, orden, destino, ubicación.

## Implementación esperada
Limitar el menú principal a los recorridos esenciales, colocar el resto en el pie de página, probar con teclado y en móvil.

## Tests que deben preverse
1. Nominal: Componer los menús y recorrerlos con el teclado y en móvil.
2. Control de rechazo: Una página despublicada desaparece del menú o se señala, nunca se sirve como 404 desde la navegación.
3. Invariante: Ningún enlace de menú apunta a un borrador o a una dirección externa no deseada.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
