# Plan de validación — Captcha

## Modelo de datos
Desafío, token, verificación en el servidor.

## Implementación esperada
Preferir campo trampa y límites nativos; un captcha de terceros exige una apertura de la política de contenido que el núcleo no delega en las extensiones.

## Tests que deben preverse
1. Nominal: Verificar que la protección elegida bloquea un envío automatizado.
2. Control de rechazo: Ningún script de captcha se carga en las páginas sin formulario.
3. Invariante: No debilitar nunca la Content-Security-Policy del sitio para cargar un script de terceros.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
