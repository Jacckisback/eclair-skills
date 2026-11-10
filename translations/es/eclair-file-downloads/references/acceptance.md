# Plan de validación — Descargas

## Modelo de datos
Archivo, título, versión, tamaño, página que lo contiene.

## Implementación esperada
Guardar los archivos públicos en la biblioteca de medios, mostrar peso y formato, versionar los archivos sustituidos.

## Tests que deben preverse
1. Nominal: Descargar cada archivo y comprobar el tipo y el tamaño anunciados.
2. Control de rechazo: Un archivo sustituido no deja la versión antigua accesible por error.
3. Invariante: Ningún archivo privado o de pago se coloca en una dirección pública adivinable.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
