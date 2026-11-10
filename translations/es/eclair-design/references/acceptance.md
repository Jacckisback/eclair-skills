# Plan de validación — Dirección artística Éclair

## Modelo de datos
Posicionamiento, identidad, tipografía, colores, componentes, fotografías y contenido real.

## Implementación esperada
Definir un universo inspirado en la actividad del cliente, componer secciones, ajustar el CSS y probar los temas con contenido real; dar prioridad a site/themes y a los bloques existentes.

## Tests que deben preverse
1. Nominal: Probar el contraste, la coherencia entre páginas y las versiones móviles.
2. Control de rechazo: La nueva apariencia sigue siendo legible sin JavaScript y respeta los enlaces existentes.
3. Invariante: No modificar nunca app/theme/ ni romper el SEO, la CSP o la ruta rápida.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
