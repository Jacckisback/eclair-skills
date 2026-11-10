# Plan de validación — Envío y transporte

## Modelo de datos
Dirección validada, zona, transportista, paquete, peso, servicio, gastos, tracking.

## Implementación esperada
Modelar las zonas y las incompatibilidades; calcular la cotización en el servidor; prever split shipments y entrega parcial; anonimizar los datos de envío en los registros.

## Tests que deben preverse
1. Nominal: Probar zona sin servicio, peso límite, dos paquetes y estado perdido.
2. Control de rechazo: Un número de seguimiento de un cliente no debe ser visible desde otra cuenta.
3. Invariante: La dirección y el seguimiento son privados; ningún dato personal en la caché pública, en logs detallados ni en URLs.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
