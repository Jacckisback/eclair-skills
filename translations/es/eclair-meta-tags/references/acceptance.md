# Plan de validación — Títulos y metadescripciones

## Modelo de datos
Título, metadescripción, expresión objetivo, vista previa del resultado.

## Implementación esperada
Redactar para cada página un título y una descripción únicos, apoyarse en la puntuación en directo del editor sin tratarla como un objetivo.

## Tests que deben preverse
1. Nominal: Controlar la unicidad y la longitud en todas las páginas.
2. Control de rechazo: Dos páginas publicadas no tienen el mismo título.
3. Invariante: Ninguna promesa de posición; ningún relleno de palabras clave.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
