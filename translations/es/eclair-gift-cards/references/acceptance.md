# Plan de validación — Tarjetas regalo

## Modelo de datos
Tarjeta, código, saldo, validez.

## Implementación esperada
Generar códigos impredecibles, llevar el saldo en el servidor, tratar la caducidad según la ley aplicable.

## Tests que deben preverse
1. Nominal: Simular compra, uso parcial y saldo restante.
2. Control de rechazo: Un código agotado o caducado se rechaza.
3. Invariante: Un código nunca es adivinable ni reutilizable más allá de su saldo.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
