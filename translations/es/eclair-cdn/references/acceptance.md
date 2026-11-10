# Plan de validación — Red de distribución (CDN)

## Modelo de datos
Zona DNS, reglas de caché, purga.

## Implementación esperada
Configurar DNS y HTTPS de extremo a extremo, excluir la administración de la caché del CDN, definir la purga al publicar.

## Tests que deben preverse
1. Nominal: Verificar las cabeceras de caché de las páginas públicas y de la administración.
2. Control de rechazo: Tras una modificación, la versión antigua deja de servirse una vez hecha la purga.
3. Invariante: La administración y toda respuesta privada nunca son almacenadas en caché por el CDN.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
