# Plan de validación — Workflows de IA

## Modelo de datos
Borrador, propuesta, validación, modelo, coste, fuente y auditoría.

## Implementación esperada
Utilizar las capacidades MCP del núcleo, mantener a una persona en el circuito, limitar acceso y presupuesto; evaluar calidad y alucinaciones.

## Tests que deben preverse
1. Nominal: Probar prompt injection, cambio de contexto y rollback.
2. Control de rechazo: Una instrucción hostil en un artículo importado no se convierte en una orden ejecutada.
3. Invariante: Ninguna IA publica, despliega, elimina o modifica PHP directamente por MCP sin control.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
