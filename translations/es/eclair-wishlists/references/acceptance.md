# Plan de validación — Listas de deseos

## Modelo de datos
Lista, producto, propietario.

## Implementación esperada
Empezar con un almacenamiento en el navegador sin cuenta; diseñar la versión con cuenta para más adelante.

## Tests que deben preverse
1. Nominal: Añadir, quitar y recuperar favoritos.
2. Control de rechazo: Un producto eliminado desaparece limpiamente de las listas.
3. Invariante: Ninguna lista se comparte ni es visible para un tercero sin una acción del propietario.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
