# Plan de validación — Alojamientos y habitaciones

## Modelo de datos
Habitación, capacidad, equipamiento, tarifas orientativas, enlace de reserva.

## Implementación esperada
Presentar cada alojamiento en una ficha, remitir al motor de reservas existente o a la solicitud por formulario.

## Tests que deben preverse
1. Nominal: Recorrer fichas y enlace de reserva en móvil.
2. Control de rechazo: Una habitación retirada deja de ofrecerse.
3. Invariante: Ninguna disponibilidad ni tarifa mostradas como garantizadas si no proceden del sistema de reservas.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
