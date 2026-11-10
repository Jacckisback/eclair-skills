# Plan de validación — Mensajería privada

## Modelo de datos
Conversación, participantes, mensaje, denuncia.

## Implementación esperada
Definir bloqueo, denuncia, límites de envío y conservación; ninguna conversación en una página en caché.

## Tests que deben preverse
1. Nominal: Simular intercambio, bloqueo y denuncia.
2. Control de rechazo: Un miembro bloqueado ya no puede escribir a quien lo ha bloqueado.
3. Invariante: Un mensaje solo es legible por sus participantes.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
