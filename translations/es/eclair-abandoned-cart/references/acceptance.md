# Plan de validación — Recuperación de carritos abandonados

## Modelo de datos
Carrito, contacto, consentimiento, recordatorio.

## Implementación esperada
Verificar la base legal, limitar el número de recordatorios, apoyarse en las herramientas del proveedor de pago cuando existan.

## Tests que deben preverse
1. Nominal: Simular abandono, recordatorio y baja.
2. Control de rechazo: Un contacto dado de baja no recibe ningún recordatorio.
3. Invariante: Ningún recordatorio sin consentimiento o base legal; baja inmediata.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
