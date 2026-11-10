# Plan de validación — Carta de restaurante

## Modelo de datos
Plato, precio, alérgenos, categoría, disponibilidad.

## Implementación esperada
Introducir la carta facilitada por el restaurador, mostrar precios y alérgenos, mantener una versión HTML legible en lugar de solo un PDF.

## Tests que deben preverse
1. Nominal: Revisar la carta publicada con el restaurador, en móvil.
2. Control de rechazo: Un plato sin información de alérgenos validada se señala, no se completa.
3. Invariante: Ningún precio ni alérgeno inventado o deducido.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
