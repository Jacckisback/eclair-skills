# Plan de validación — Formularios con archivos adjuntos

## Modelo de datos
Archivo enviado, tipo, tamaño, propietario, periodo de conservación.

## Implementación esperada
Definir los tipos y tamaños aceptados, el almacenamiento fuera de la raíz pública, el análisis y la eliminación automática.

## Tests que deben preverse
1. Nominal: Enviar un archivo válido y encontrarlo en la administración.
2. Control de rechazo: Un archivo demasiado pesado, camuflado o ejecutable es rechazado.
3. Invariante: Ningún archivo enviado es ejecutable ni se sirve directamente al público.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
