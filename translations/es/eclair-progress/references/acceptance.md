# Plan de validación — Seguimiento del progreso

## Modelo de datos
Inscripción, unidad, estado de finalización, intento, duración, revisión.

## Implementación esperada
Definir reglas de finalización; registrar el progreso bajo control de acceso; versionar las unidades; agregar el progreso calculado a partir de estados autorizados.

## Tests que deben preverse
1. Nominal: Probar reanudación de sesión, dos dispositivos, lección retirada.
2. Control de rechazo: Dos dispositivos no deben hacer retroceder el progreso ya validado.
3. Invariante: El progreso es un dato individual no cacheable; no aceptar nunca un identificador de miembro arbitrario.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
