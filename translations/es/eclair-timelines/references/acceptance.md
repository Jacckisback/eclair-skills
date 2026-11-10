# Plan de validación — Líneas de tiempo

## Modelo de datos
Etapa, fecha, título, texto.

## Implementación esperada
Renderizar la línea de tiempo como lista ordenada con estilos CSS, legible en columna en móvil.

## Tests que deben preverse
1. Nominal: Comprobar el orden de lectura y la visualización en móvil.
2. Control de rechazo: Una etapa sin fecha sigue siendo legible y ordenada.
3. Invariante: Las fechas y los hechos mostrados los proporciona el cliente.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
