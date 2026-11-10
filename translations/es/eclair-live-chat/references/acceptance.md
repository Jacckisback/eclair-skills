# Plan de validación — Chat en directo

## Modelo de datos
Canal, horario, enlace de conversación.

## Implementación esperada
Preferir un enlace a un servicio de mensajería (WhatsApp, correo electrónico, teléfono) con horario; un widget de terceros depende de la política de contenido nativa.

## Tests que deben preverse
1. Nominal: Abrir el canal desde móvil y ordenador.
2. Control de rechazo: Fuera de horario, el sitio lo anuncia en lugar de prometer una respuesta inmediata.
3. Invariante: Ningún widget carga un rastreador antes de una acción del visitante.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
