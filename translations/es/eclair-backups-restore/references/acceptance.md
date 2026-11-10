# Plan de validación — Copias de seguridad y restauración

## Modelo de datos
Archivo de copia de seguridad, fecha, destino, prueba de restauración.

## Implementación esperada
Activar la copia de seguridad descargable o hacia el almacenamiento remoto previsto por el núcleo, fijar la frecuencia, restaurar en una copia para verificar.

## Tests que deben preverse
1. Nominal: Restaurar la última copia de seguridad en una instalación de prueba y comparar.
2. Control de rechazo: Un archivo modificado o malicioso se rechaza en la restauración.
3. Invariante: Una copia de seguridad contiene datos personales: se almacena cifrada o en lugar seguro, nunca en una carpeta pública.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
