# Plan de validación — Llamadas a la acción

## Modelo de datos
Título, texto, botón, destino.

## Implementación esperada
Definir una acción principal por página, repetirla en los lugares adecuados, comprobar el contraste y que el texto del botón sea explícito.

## Tests que deben preverse
1. Nominal: Seguir cada botón hasta su destino en móvil.
2. Control de rechazo: Un botón sin destino válido no se publica.
3. Invariante: Ningún enlace engañoso ni redirección abierta.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
