# Plan de validación — Formulario de contacto

## Modelo de datos
Mensaje, nombre, correo electrónico, asunto, fecha, estado de lectura.

## Implementación esperada
Colocar el bloque de contacto nativo, configurar el destinatario, probar el envío y la recepción, mostrar la cláusula informativa.

## Tests que deben preverse
1. Nominal: Enviar un mensaje real y encontrarlo en la administración y por correo electrónico.
2. Control de rechazo: Los envíos repetidos en ráfaga son limitados por el núcleo.
3. Invariante: Los mensajes solo son visibles para las cuentas que tienen el permiso Mensajes.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
