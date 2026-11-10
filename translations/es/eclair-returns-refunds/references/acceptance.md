# Plan de validación — Devoluciones y reembolsos

## Modelo de datos
Solicitud de devolución, motivo, estado, reembolso.

## Implementación esperada
Publicar la política de devoluciones nativa en las fichas, tramitar las solicitudes mediante el formulario de contacto, reembolsar en el proveedor; diseñar el seguimiento estructurado.

## Tests que deben preverse
1. Nominal: Recorrer una solicitud de devolución desde la recepción hasta el reembolso.
2. Control de rechazo: Una solicitud fuera de plazo recibe una respuesta motivada, no un reembolso automático.
3. Invariante: Un reembolso solo lo inicia una persona habilitada, en el proveedor.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
