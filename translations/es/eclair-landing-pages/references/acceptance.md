# Plan de validación — Páginas de aterrizaje

## Modelo de datos
Promesa, pruebas, oferta, llamada a la acción.

## Implementación esperada
Escribir una página para una sola intención, componerla con bloques nativos, vincular la acción a un formulario o a un enlace de pago.

## Tests que deben preverse
1. Nominal: Recorrer la página en móvil hasta la acción.
2. Control de rechazo: Una prueba no proporcionada por el cliente no aparece.
3. Invariante: Ningún testimonio, cifra o garantía inventados.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
