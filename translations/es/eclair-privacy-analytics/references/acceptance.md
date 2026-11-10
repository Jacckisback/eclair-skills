# Plan de validación — Medición de audiencia respetuosa

## Modelo de datos
Página vista, origen, periodo, agregados.

## Implementación esperada
Preferir los registros del servidor o una herramienta sin cookies autoalojada; un script de terceros depende de la política de contenido nativa.

## Tests que deben preverse
1. Nominal: Comparar las páginas vistas medidas con un recorrido de prueba.
2. Control de rechazo: La medición no instala ninguna cookie.
3. Invariante: No se conserva ninguna dirección IP completa ni ningún identificador de visitante.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
