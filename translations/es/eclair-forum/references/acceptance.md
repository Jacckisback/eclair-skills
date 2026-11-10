# Plan de validación — Arquitectura Foro

## Modelo de datos
Espacio, categoría, tema, mensaje, autor, rol, denuncia, bloqueo.

## Implementación esperada
Separar temas indexables y privados; prever paginación estable, permisos por objeto, cuotas y moderación; preparar un motor de búsqueda acotado.

## Tests que deben preverse
1. Nominal: Probar visitante, miembro, moderador y cuenta suspendida.
2. Control de rechazo: Tema privado inexistente para un miembro no autorizado, incluso a través de la búsqueda.
3. Invariante: Ninguna escritura anónima sin antispam, CSRF y limitación de frecuencia; nunca HTML arbitrario ejecutado.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
