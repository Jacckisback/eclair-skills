# Plan de validación — Sistema de diseño

## Modelo de datos
Tokens, cuadrícula, espaciados, colores, tipografía, componentes y estados.

## Implementación esperada
Declarar la escala de tokens, reutilizar componentes, documentar estados y variantes; compatibilidad con el tema Éclair.

## Tests que deben preverse
1. Nominal: Probar el contraste, la coherencia y el cambio de tema.
2. Control de rechazo: Cambiar el color principal no provoca ninguna ilegibilidad de los enlaces ni de los errores.
3. Invariante: No introducir ninguna hoja CSS pesada ni biblioteca JS sin prueba de su necesidad.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
