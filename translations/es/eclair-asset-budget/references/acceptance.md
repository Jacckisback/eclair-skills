# Plan de validación — Presupuesto de peso

## Modelo de datos
Presupuesto por tipo de recurso, medición, desviación.

## Implementación esperada
Fijar presupuestos por tipo de página, medir con la herramienta del núcleo, rechazar todo añadido que los supere sin justificación.

## Tests que deben preverse
1. Nominal: Lanzar la medición de los presupuestos en el sitio y en el paquete producido.
2. Control de rechazo: Un paquete que supera el presupuesto no se entrega tal cual.
3. Invariante: Ninguna dependencia de terceros cargada para una función decorativa.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
