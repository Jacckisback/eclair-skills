# Plan de validación — Medios didácticos

## Modelo de datos
Lección, medio, transcripción, archivos descargables, permisos y duración.

## Implementación esperada
Preparar medios y subtítulos accesibles; prever una distribución con autorización en el servidor o una URL firmada de corta duración; separar CDN público y contenido reservado.

## Tests que deben preverse
1. Nominal: Probar medio caducado, acceso sin inscripción y móvil.
2. Control de rechazo: Una URL de documento privado copiada en otro navegador se rechaza o caduca.
3. Invariante: Ocultar un enlace en el HTML no es una protección; no colocar el medio privado en /media público.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
