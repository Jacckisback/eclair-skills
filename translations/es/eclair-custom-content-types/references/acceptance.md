# Plan de validación — Tipos de contenido personalizados

## Modelo de datos
Ficha de negocio, campos, listado, dirección, estado.

## Implementación esperada
Elegir entre páginas con bloques dedicados y una extensión con almacenamiento propio y rutas GET, fijar las direcciones, prever listado y ficha.

## Tests que deben preverse
1. Nominal: Crear un tipo de ficha mediante una extensión, con listado y detalle en GET, y después validar el paquete.
2. Control de rechazo: Una ficha no publicada no se sirve ni en el listado ni por su dirección directa.
3. Invariante: No escribir nunca en los archivos de contenidos del núcleo desde una extensión.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
