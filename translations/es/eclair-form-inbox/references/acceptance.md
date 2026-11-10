# Plan de validación — Mensajes recibidos

## Modelo de datos
Mensaje, estado, respuesta, periodo de conservación.

## Implementación esperada
Definir quién lee y responde, en qué plazo, cuánto tiempo se conservan los mensajes y cómo se eliminan.

## Tests que deben preverse
1. Nominal: Tramitar un mensaje desde la recepción hasta el archivado.
2. Control de rechazo: Una cuenta sin el permiso Mensajes no accede a ningún mensaje.
3. Invariante: Periodo de conservación limitado y permiso de acceso restringido.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
