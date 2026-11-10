# Plan de validación — Enlaces de afiliación

## Modelo de datos
Enlace, programa, mención, contenido que lo incluye.

## Implementación esperada
Activar la extensión de afiliación incluida, declarar los programas, dejar que el núcleo añada la mención y el atributo de patrocinio.

## Tests que deben preverse
1. Nominal: Publicar una comparativa y comprobar la mención y los atributos de los enlaces.
2. Control de rechazo: Un enlace de afiliación nunca se presenta como una opinión independiente.
3. Invariante: Ningún enlace de afiliación sin mención publicitaria visible.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
