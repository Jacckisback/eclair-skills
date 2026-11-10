# Plan de validación — Observabilidad y alertas

## Modelo de datos
Logs estructurados, errores, correlaciones, métricas, trazas, conservación.

## Implementación esperada
Definir alertas útiles, anonimizar los datos, supervisar tareas y caché, distinguir incidente del sitio y del módulo, proporcionar un runbook.

## Tests que deben preverse
1. Nominal: Probar aumento de errores 5xx, retraso de las tareas y disco lleno.
2. Control de rechazo: Un módulo desactivado no sigue enviando datos ni ejecutando tareas.
3. Invariante: Ninguna contraseña, token, pago o PII en bruto en los logs; sin telemetría oculta.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
