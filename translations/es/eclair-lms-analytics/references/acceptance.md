# Plan de validación — Panel de control pedagógico

## Modelo de datos
Inscripciones, progreso, resultados agregados, eventos de curso.

## Implementación esperada
Definir métricas útiles para los formadores, filtrar por curso y autorización; reducir la recogida; prever conservación y exportación.

## Tests que deben preverse
1. Nominal: Probar la visibilidad del formador en el curso A frente al B.
2. Control de rechazo: Una consulta de estadísticas agregadas no debe exponer la identidad de otro estudiante.
3. Invariante: Las estadísticas de un alumno solo son visibles para las partes autorizadas.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
