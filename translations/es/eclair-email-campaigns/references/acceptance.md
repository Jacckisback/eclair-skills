# Plan de validación — Campañas de correo electrónico

## Modelo de datos
Lista, segmento, campaña, envío, baja.

## Implementación esperada
Confiar el envío a un servicio especializado, preparar los contenidos desde el sitio, definir segmentos, frecuencia y baja.

## Tests que deben preverse
1. Nominal: Enviar una campaña de prueba a una lista interna.
2. Control de rechazo: Una dirección dada de baja ya no recibe nada.
3. Invariante: Cada correo contiene un enlace de baja que funciona; ninguna lista comprada.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
