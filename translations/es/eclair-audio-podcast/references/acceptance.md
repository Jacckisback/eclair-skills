# Plan de validación — Audio y pódcast

## Modelo de datos
Episodio, archivo de audio, duración, notas, feed.

## Implementación esperada
Crear una página por episodio con reproductor HTML nativo, generar el feed de pódcast en GET y alojar los archivos pesados fuera del sitio si es necesario.

## Tests que deben preverse
1. Nominal: Validar el feed con un validador de pódcast y reproducir un episodio en móvil.
2. Control de rechazo: Un episodio en borrador no figura en el feed.
3. Invariante: El feed solo referencia episodios publicados y archivos públicos.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
