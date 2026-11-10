# Plan de validación — Redirecciones

## Modelo de datos
Dirección antigua, dirección nueva, tipo, fecha.

## Implementación esperada
Importar las direcciones antiguas, crear una redirección directa por dirección, eliminar cadenas y bucles.

## Tests que deben preverse
1. Nominal: Probar un lote de direcciones antiguas y anotar estado y destino.
2. Control de rechazo: Ninguna cadena de más de un salto ni ningún bucle.
3. Invariante: Ninguna redirección abierta hacia un dominio no deseado.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
