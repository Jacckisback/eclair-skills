# Plan de validación — Datos estructurados

## Modelo de datos
WebPage, Article, Product, FAQ pertinente, Organization, BreadcrumbList.

## Implementación esperada
Inspeccionar el JSON-LD nativo antes de añadir un tipo; evitar la duplicación; alinear cada campo con los datos visibles y las directrices de los buscadores.

## Tests que deben preverse
1. Nominal: Probar JSON válido, canonical, identificadores y contenido mostrado.
2. Control de rechazo: Ningún precio/opinión/product inventado o ausente de la página figura en el JSON-LD.
3. Invariante: Éclair v2 todavía no expone todas las contribuciones JSON-LD a las extensiones; proponer una RFC en lugar de una inyección opaca.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
