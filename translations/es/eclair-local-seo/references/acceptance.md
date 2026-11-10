# Plan de validación — SEO local

## Modelo de datos
Nombre, dirección, teléfono, horarios, zona atendida.

## Implementación esperada
Introducir los datos de contacto exactos en los ajustes, comprobar el marcado de empresa local generado por el núcleo, alinear la ficha de empresa y el sitio.

## Tests que deben preverse
1. Nominal: Comparar los datos de contacto del sitio, del marcado y de la ficha de empresa.
2. Control de rechazo: Los horarios no confirmados no se publican.
3. Invariante: Ninguna dirección, opinión o zona de servicio inventadas.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
