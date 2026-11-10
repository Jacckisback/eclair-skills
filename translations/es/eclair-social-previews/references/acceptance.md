# Plan de validación — Vistas previas al compartir

## Modelo de datos
Título para compartir, descripción, imagen para compartir.

## Implementación esperada
Comprobar las etiquetas para compartir y la imagen generada por el núcleo, probar la vista previa en las principales plataformas.

## Tests que deben preverse
1. Nominal: Probar la vista previa de un artículo y de una página.
2. Control de rechazo: Una página sin imagen propia conserva una vista previa correcta por defecto.
3. Invariante: La imagen para compartir no contiene ningún dato personal ni texto engañoso.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
