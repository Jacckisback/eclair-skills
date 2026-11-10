# Plan de validación — Plataformas de automatización

## Modelo de datos
Escenario, activador, datos transmitidos.

## Implementación esperada
Exponer en lectura lo que la plataforma puede consultar (feeds, JSON público); diseñar la recepción de eventos para más adelante.

## Tests que deben preverse
1. Nominal: Hacer que la plataforma lea un feed público y active un escenario.
2. Control de rechazo: Una llamada entrante no autenticada no modifica nada en el sitio.
3. Invariante: Ningún dato personal se expone en un punto de acceso público para facilitar una automatización.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
