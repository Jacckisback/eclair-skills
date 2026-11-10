# Plan de validación — Ajustes del sitio

## Modelo de datos
Nombre, descripción, logotipo, datos de contacto, idioma, tema, dirección artística.

## Implementación esperada
Leer las capacidades del sitio, rellenar los ajustes desde la administración, previsualizar antes de guardar.

## Tests que deben preverse
1. Nominal: Configurar un sitio nuevo y verificar la presentación pública.
2. Control de rechazo: Una cuenta sin permiso Ajustes no modifica ningún ajuste.
3. Invariante: Ninguna protección nativa se desactiva para ganar tiempo.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
