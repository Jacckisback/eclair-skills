# Plan de validación — Arquitectura LMS

## Modelo de datos
Cursos, secciones, lecciones, requisitos previos, inscripciones, progreso, permisos y posibles ventas.

## Implementación esperada
Definir catálogos públicos frente a lecciones privadas; elegir un almacenamiento de progreso transaccional; vincular el acceso a la identidad de miembro validada; componer módulos independientes.

## Tests que deben preverse
1. Nominal: Probar estudiante, profesor, administrador y visitante.
2. Control de rechazo: Un alumno inscrito no puede leer el contenido privado de otro curso.
3. Invariante: Ninguna promesa de acceso privado mediante una simple URL secreta o un bloque oculto.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
