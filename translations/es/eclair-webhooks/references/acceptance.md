# Plan de validación — Webhooks entrantes y salientes

## Modelo de datos
Origen, secreto, evento, firma, marca de tiempo, ID único, intento, resultado.

## Implementación esperada
Especificar el contrato, verificar la firma sobre los bytes en bruto, protección contra repetición y cola duradera; documentar retries/dlq y endpoint POST privado.

## Tests que deben preverse
1. Nominal: Probar envío doble, retraso, orden invertido y secreto cambiado.
2. Control de rechazo: Dos intentos del mismo webhook solo desencadenan una única mutación de negocio.
3. Invariante: No publicar nunca un webhook con el secreto en la URL ni procesar un evento financiero sin firmar.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
