# Plan de validación — Visor de imágenes

## Modelo de datos
Imagen, versión ampliada, leyenda.

## Implementación esperada
Utilizar dialog nativo o un enlace a la imagen, gestionar el foco, la tecla Escape y el retorno, sin dependencias.

## Tests que deben preverse
1. Nominal: Abrir, navegar y cerrar con el teclado.
2. Control de rechazo: Sin JavaScript, el clic simplemente abre la imagen.
3. Invariante: El foco queda atrapado y después se devuelve correctamente; ningún contenido externo.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
