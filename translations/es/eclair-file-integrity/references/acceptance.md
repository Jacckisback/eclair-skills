# Plan de validación — Integridad de los archivos

## Modelo de datos
Archivo, huella esperada, desviación.

## Implementación esperada
Lanzar el control de integridad de la página Seguridad, explicar cada desviación, restaurar los archivos originales si hace falta.

## Tests que deben preverse
1. Nominal: Modificar un archivo en una copia de prueba y comprobar la alerta.
2. Control de rechazo: Un archivo del núcleo alterado nunca se declara conforme.
3. Invariante: Una desviación inexplicada se trata como un incidente, no se ignora.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
