# Plan de validación — Cuestionarios y certificados

## Modelo de datos
Pregunta, opción, corrección, intento, puntuación, plazo, certificado y verificación.

## Implementación esperada
Versionar el banco de preguntas; calificar en el servidor; definir intentos y tiempo; generar un certificado firmado/verificable sin PII pública.

## Tests que deben preverse
1. Nominal: Probar trampas, fin de sesión, validación del certificado.
2. Control de rechazo: Enviar dos veces un intento no debe generar dos certificados.
3. Invariante: No enviar nunca la solución ni la respuesta correcta en el HTML de una prueba activa.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
