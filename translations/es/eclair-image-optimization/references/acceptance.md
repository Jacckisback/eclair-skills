# Plan de validación — Optimización de imágenes

## Modelo de datos
Imagen de origen, variantes responsive, dimensiones, peso.

## Implementación esperada
Proporcionar originales del tamaño adecuado, dejar que el núcleo genere las variantes, controlar el peso real servido en móvil.

## Tests que deben preverse
1. Nominal: Medir el peso y las dimensiones servidos en móvil y en ordenador.
2. Control de rechazo: Ninguna imagen se sirve sin dimensiones explícitas.
3. Invariante: Los metadatos sensibles (geolocalización) no se publican.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
