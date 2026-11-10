# Plan de validación — Anuncios inmobiliarios

## Modelo de datos
Inmueble, operación, geolocalización redondeada, superficie, medio, precio, disponibilidad.

## Implementación esperada
Versionar los anuncios, proporcionar filtros acotados, gestionar el estado vendido/alquilado, las imágenes y las solicitudes de visita.

## Tests que deben preverse
1. Nominal: Probar anuncios retirados, medios privados y filtros.
2. Control de rechazo: Un inmueble eliminado deja de aparecer en los resultados y en la caché tras la purga.
3. Invariante: No exponer direcciones exactas ni datos de contacto de los propietarios sin finalidad ni autorización.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
