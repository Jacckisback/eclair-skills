# Plan de validación — Etiquetas y taxonomías

## Modelo de datos
Término, tipo de taxonomía, contenidos vinculados, dirección de archivo.

## Implementación esperada
Inventariar las taxonomías existentes, fusionar las que dupliquen las categorías, proponer páginas de agrupación en GET para el resto y redirigir los archivos antiguos.

## Tests que deben preverse
1. Nominal: Convertir un conjunto de etiquetas en categorías o en páginas de agrupación y comprobar las redirecciones.
2. Control de rechazo: Un antiguo archivo de etiqueta eliminado redirige a la página más cercana, sin cadena.
3. Invariante: No generar cientos de archivos pobres indexables.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
