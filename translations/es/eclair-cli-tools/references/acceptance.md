# Plan de validación — Herramientas de línea de comandos

## Modelo de datos
Comando, entrada, salida, código de retorno.

## Implementación esperada
En un checkout del núcleo, lanzar el validador, la suite de tests y la medición de los presupuestos; integrar estos comandos en la CI del proyecto.

## Tests que deben preverse
1. Nominal: Validar un paquete y leer el informe JSON.
2. Control de rechazo: Un paquete no válido hace fallar el comando y la CI.
3. Invariante: Ningún comando se lanza en producción sin copia de seguridad.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
