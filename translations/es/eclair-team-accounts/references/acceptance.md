# Plan de validación — Cuentas del equipo

## Modelo de datos
Cuenta, permisos, autenticación en dos pasos, último inicio de sesión.

## Implementación esperada
Enumerar quién hace qué, asignar los permisos nativos mínimos, imponer la autenticación en dos pasos, retirar las cuentas innecesarias.

## Tests que deben preverse
1. Nominal: Crear una cuenta de redactor y verificar lo que puede y lo que no puede hacer.
2. Control de rechazo: Una cuenta sin permiso Ajustes no puede ni activar una extensión ni cambiar de tema.
3. Invariante: Ninguna cuenta compartida; ningún permiso Seguridad concedido por comodidad.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
