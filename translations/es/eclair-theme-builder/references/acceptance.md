# Plan de validación — Creación de temas

## Modelo de datos
theme.json, estilos, assets, templates declarados, licencia y procedencia.

## Implementación esperada
Partir del tema de ejemplo oficial, emplear las variables y plantillas admitidas, probar la preview y después el ZIP, comprobar la compatibilidad de versión.

## Tests que deben preverse
1. Nominal: Probar el validador de temas, la activación, la previsualización y la vuelta atrás.
2. Control de rechazo: Un template defectuoso no deja el sitio inaccesible gracias a la alternativa prevista.
3. Invariante: No rehacer nunca el SEO head ni el canonical ni tocar los archivos del núcleo.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
