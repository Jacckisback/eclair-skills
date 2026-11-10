# Plan de validación — Search Console

## Modelo de datos
Propiedad, método de verificación, sitemap declarado, informes.

## Implementación esperada
Verificar el dominio mediante registro DNS, declarar el sitemap nativo, leer cobertura y consultas cada mes.

## Tests que deben preverse
1. Nominal: Verificar la propiedad y que el sitemap se tiene en cuenta.
2. Control de rechazo: Un error de cobertura se explica, no se oculta.
3. Invariante: Ningún acceso de propietario concedido a un tercero sin el acuerdo del cliente.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
