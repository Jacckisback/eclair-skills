# Plan de validación — Vídeos

## Modelo de datos
Vídeo, fuente, imagen de vista previa, subtítulos.

## Implementación esperada
Utilizar el bloque de vídeo nativo, preferir una fachada en la que se pueda hacer clic para las plataformas de terceros, proporcionar subtítulos o transcripción.

## Tests que deben preverse
1. Nominal: Comprobar que no sale ninguna petición a terceros antes del clic.
2. Control de rechazo: Una dirección de vídeo de un dominio no autorizado es rechazada.
3. Invariante: Ningún reproductor de terceros se carga antes del clic del visitante.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
