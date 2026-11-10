# Plan de validación — Publicidad

## Modelo de datos
Ubicación, consentimiento, archivo ads.txt.

## Implementación esperada
Utilizar la página Publicidad nativa, limitar las ubicaciones, comprobar el consentimiento, la etiqueta y el impacto en la velocidad.

## Tests que deben preverse
1. Nominal: Medir la página con y sin publicidad y comprobar el consentimiento.
2. Control de rechazo: Las páginas que no son artículos no muestran publicidad.
3. Invariante: Ninguna publicidad se carga antes del consentimiento requerido.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
