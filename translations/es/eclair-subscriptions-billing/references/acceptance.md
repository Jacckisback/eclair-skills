# Plan de validación — Suscripciones de pago

## Modelo de datos
Oferta, periodo, suscriptor, vencimiento, estado.

## Implementación esperada
Dejar que el proveedor gestione los cobros y el área de cliente; diseñar la sincronización de los permisos mediante eventos firmados.

## Tests que deben preverse
1. Nominal: Simular alta, renovación, fallo y cancelación.
2. Control de rechazo: Un pago fallido no prolonga ningún acceso.
3. Invariante: Un permiso de acceso solo se abre con un evento de pago autenticado.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
