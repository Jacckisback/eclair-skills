# Plan de validación — Glosario

## Modelo de datos
Término, definición, términos relacionados.

## Implementación esperada
Redactar una definición clara por término, clasificar por orden alfabético, enlazar los términos con los contenidos que los emplean.

## Tests que deben preverse
1. Nominal: Navegar por letra y seguir los enlaces entre términos.
2. Control de rechazo: Un término sin definición validada no se publica.
3. Invariante: Ninguna definición copiada de una fuente protegida.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
