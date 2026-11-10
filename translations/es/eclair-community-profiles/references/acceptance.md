# Plan de validación — Perfiles de comunidad

## Modelo de datos
Apodo único, avatar, preferencias de visibilidad, reputación y roles.

## Implementación esperada
Distinguir ID interno y apodo; imponer límites y moderación del avatar; exponer únicamente los campos consentidos; gestionar cambios de nombre y redirecciones seguras.

## Tests que deben preverse
1. Nominal: Probar colisión de apodos y eliminación de cuenta.
2. Control de rechazo: Un visitante no puede inferir un email a partir de un mensaje de error o de una API de perfil.
3. Invariante: Email, sesión, IP, dirección e información de recuperación permanecen privados.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
