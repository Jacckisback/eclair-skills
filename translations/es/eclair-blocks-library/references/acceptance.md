# Plan de validación — Biblioteca de bloques

## Modelo de datos
Tipo con espacio de nombres, declaración de los campos, límites, renderizado y datos conservados.

## Implementación esperada
Dar prioridad a los bloques nativos; declarar los campos autorizados; generar un renderizado escapado, valores por defecto y conservación tras la desactivación.

## Tests que deben preverse
1. Nominal: Probar campos no válidos, la eliminación de la extensión y la reinstalación.
2. Control de rechazo: El bloque desactivado se conserva, pero ni se ejecuta ni se renderiza.
3. Invariante: Rechazar la ejecución de HTML/JS procedente de campos; ninguna pérdida de datos cuando falta el bloque.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
