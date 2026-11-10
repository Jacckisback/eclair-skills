# Plan de validación — Formularios y mini-CRM

## Modelo de datos
Formulario, campo, consentimiento, contacto, origen, ticket y estado.

## Implementación esperada
Definir finalidad y plazo de conservación por formulario; validar los datos en el servidor; proteger contra el spam; aislar los archivos y el permiso de lectura.

## Tests que deben preverse
1. Nominal: Probar spam, archivo adjunto, duplicado y supresión RGPD.
2. Control de rechazo: Un usuario sin permiso no puede exportar la base de contactos.
3. Invariante: Un formulario público no debe permitir la inyección de email ni hacer aparecer los datos en la caché.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
