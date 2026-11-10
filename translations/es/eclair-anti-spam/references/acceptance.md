# Plan de validación — Protección contra el spam

## Modelo de datos
Mensaje, token de formulario, límite de frecuencia.

## Implementación esperada
Apoyarse en el token y los límites del formulario nativo, añadir si hace falta un campo trampa, vigilar la bandeja de entrada.

## Tests que deben preverse
1. Nominal: Enviar un mensaje legítimo y después una ráfaga automatizada.
2. Control de rechazo: Un envío sin token válido se rechaza.
3. Invariante: Ningún servicio de terceros recibe los mensajes de los visitantes sin información previa.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
