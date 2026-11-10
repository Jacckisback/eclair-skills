# Plan de validación — Biblioteca de medios

## Modelo de datos
Archivo, texto alternativo, dimensiones, usos.

## Implementación esperada
Importar los medios, rellenar los textos alternativos, localizar los archivos sin usar y los duplicados.

## Tests que deben preverse
1. Nominal: Subir varios formatos y comprobar la conversión, las dimensiones y los textos alternativos.
2. Control de rechazo: Un archivo con formato prohibido o malicioso es rechazado en la subida.
3. Invariante: Solo se suben los formatos aceptados por el núcleo; ningún archivo ejecutable.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
