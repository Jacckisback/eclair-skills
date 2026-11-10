# Plan de validación — Inscripciones a los cursos

## Modelo de datos
Miembro, curso, inscripción, estado, origen, fecha y revocación.

## Implementación esperada
Crear una inscripción idempotente; tratar los permisos por objeto; distinguir inscripción gratuita/de pago; revocar tras un reembolso según una regla explícita.

## Tests que deben preverse
1. Nominal: Probar compra doble, reembolso, suspensión de la cuenta.
2. Control de rechazo: Un miembro dado de baja ya no puede acceder a las lecciones antes autorizadas.
3. Invariante: Nunca una inscripción automática a partir de una simple URL de retorno del proveedor de pago.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
