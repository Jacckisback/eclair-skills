# Plan de validación — Botones para compartir

## Modelo de datos
Red, dirección para compartir, etiqueta.

## Implementación esperada
Utilizar simples enlaces para compartir y la API de compartir del navegador como mejora progresiva.

## Tests que deben preverse
1. Nominal: Compartir una página desde móvil y desde ordenador.
2. Control de rechazo: Ninguna petición a terceros antes del clic.
3. Invariante: Ningún botón carga scripts ni rastreadores de terceros.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
