# Plan de validación — Eventos y entradas

## Modelo de datos
Evento, sesión, tipo de plaza, reserva, entrada, escaneo, reembolso.

## Implementación esperada
Separar los cupos por sesión; emitir entradas únicas tras el pago confirmado; gestionar un control de acceso atómico y la transferencia.

## Tests que deben preverse
1. Nominal: Probar doble escaneo, cancelación y última entrada simultánea.
2. Control de rechazo: Misma entrada presentada en dos puertas => una sola admisión aceptada.
3. Invariante: El código QR no contiene datos personales en claro y no autoriza varias entradas.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
