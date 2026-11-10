# Plan de validación — Logotipos de clientes y socios

## Modelo de datos
Logotipo, nombre, enlace opcional.

## Implementación esperada
Mostrar los logotipos en cuadrícula estática, tamaños homogéneos, nombres como texto alternativo.

## Tests que deben preverse
1. Nominal: Comprobar la legibilidad en modo claro y oscuro.
2. Control de rechazo: Un logotipo sin autorización registrada no se integra.
3. Invariante: Solo se publican los logotipos cuyo uso está autorizado.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
