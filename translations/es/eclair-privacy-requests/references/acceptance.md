# Plan de validación — Solicitudes relativas a los datos

## Modelo de datos
Solicitud, persona, datos afectados, plazo, respuesta.

## Implementación esperada
Cartografiar dónde están los datos (mensajes, cuentas, registros, copias de seguridad), redactar el procedimiento de acceso y de supresión, llevar un registro.

## Tests que deben preverse
1. Nominal: Recorrer una solicitud de acceso y después de supresión sobre un conjunto de prueba.
2. Control de rechazo: Una solicitud sin verificación de identidad no da lugar a ninguna divulgación.
3. Invariante: La identidad del solicitante se verifica antes de cualquier comunicación de datos.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
