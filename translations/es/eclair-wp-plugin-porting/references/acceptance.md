# Plan de validación — Portabilidad de extensiones de WordPress

## Modelo de datos
Extensión de origen, funciones realmente utilizadas, equivalente nativo, diferencia.

## Implementación esperada
Enumerar lo que la extensión hace realmente en el sitio, buscar primero la función nativa, si no el skill del catálogo, si no una extensión a medida; no copiar nunca código PHP de WordPress.

## Tests que deben preverse
1. Nominal: Elaborar la tabla de correspondencias de un sitio real y hacerla validar.
2. Control de rechazo: Una función sin equivalente se anuncia como ausente, no se simula.
3. Invariante: No se reutiliza ningún código con licencia incompatible o dependiente de la API de WordPress.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
