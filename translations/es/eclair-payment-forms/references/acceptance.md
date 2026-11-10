# Plan de validación — Formularios de pago

## Modelo de datos
Servicio, importe, enlace de pago del proveedor.

## Implementación esperada
Crear el enlace en el proveedor de pagos, mostrarlo en una página clara con las condiciones, no almacenar nada en el sitio.

## Tests que deben preverse
1. Nominal: Pagar en modo de prueba y comprobar el recibo y la página de retorno.
2. Control de rechazo: Un importe modificado en el navegador no tiene ningún efecto sobre el importe cobrado.
3. Invariante: Ningún dato bancario transita por el sitio ni se almacena en él.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
