# Plan de validación — Solicitudes de presupuesto

## Modelo de datos
Solicitud, servicio, presupuesto disponible, plazo, datos de contacto.

## Implementación esperada
Empezar con el formulario de contacto nativo y preguntas guiadas en la página; diseñar el formulario estructurado para más adelante.

## Tests que deben preverse
1. Nominal: Enviar una solicitud tipo y comprobar que se recibe completa.
2. Control de rechazo: Una solicitud sin datos de contacto válidos es rechazada con un mensaje claro.
3. Invariante: Solo se piden los datos útiles para el presupuesto.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
