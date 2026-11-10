# Plan de validación — Pruebas A/B

## Modelo de datos
Variante, reparto, objetivo, resultado.

## Implementación esperada
Probar por periodos sucesivos o por direcciones distintas en lugar de por variantes en la caché; fijar de antemano la hipótesis, la duración y la medición.

## Tests que deben preverse
1. Nominal: Llevar a cabo una prueba con dos páginas de aterrizaje distintas.
2. Control de rechazo: Un resultado sin volumen suficiente no se presenta como concluyente.
3. Invariante: Ninguna variante se almacena en la caché compartida en función del visitante.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
