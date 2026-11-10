# Plan de validación — Métricas web esenciales

## Modelo de datos
Renderizado del elemento más grande, estabilidad, capacidad de respuesta, por plantilla.

## Implementación esperada
Medir en laboratorio y con datos reales cuando existan, tratar la causa principal por plantilla, volver a medir.

## Tests que deben preverse
1. Nominal: Medir tres plantillas en móvil antes y después de la corrección.
2. Control de rechazo: Una mejora no medida no se anuncia como conseguida.
3. Invariante: No se promete ninguna puntuación; solo se comunican los resultados medidos.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
