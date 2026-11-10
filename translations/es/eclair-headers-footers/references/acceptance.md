# Plan de validación — Cabeceras y pies de página

## Modelo de datos
Logotipo, menú, datos de contacto, enlaces legales.

## Implementación esperada
Pasar por un paquete de tema en site/themes, respetar las variables del contrato de tema, mantener el enlace de salto y los enlaces legales.

## Tests que deben preverse
1. Nominal: Validar el tema y comprobar la cabecera y el pie de página en todas las páginas tipo.
2. Control de rechazo: El tema rechazado por el validador no se entrega.
3. Invariante: No generar nunca por cuenta propia etiquetas SEO o cabeceras que el núcleo ya proporciona.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
