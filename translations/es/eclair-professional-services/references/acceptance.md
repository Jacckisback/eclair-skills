# Plan de validación — Sitio de profesión liberal

## Modelo de datos
Servicio, profesional, honorarios orientativos, toma de contacto.

## Implementación esperada
Presentar ámbitos de actuación y trayectorias reales, respetar las normas de comunicación de la profesión, ofrecer contacto o cita.

## Tests que deben preverse
1. Nominal: Hacer que el profesional revise los contenidos.
2. Control de rechazo: Una especialidad no reconocida no se muestra como título.
3. Invariante: Ninguna promesa de resultado ni mención prohibida por la deontología de la profesión.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
