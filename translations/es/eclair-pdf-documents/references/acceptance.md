# Plan de validación — Documentos PDF

## Modelo de datos
Documento, título, resumen, página de presentación, archivo.

## Implementación esperada
Crear una página HTML de presentación por documento con resumen, enlace de descarga y alternativa accesible.

## Tests que deben preverse
1. Nominal: Comprobar el enlace, el peso, el título del documento y la página de presentación.
2. Control de rechazo: Un PDF retirado devuelve una respuesta limpia y no un enlace roto en las páginas.
3. Invariante: Ningún PDF que contenga datos personales se publica sin consentimiento.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
