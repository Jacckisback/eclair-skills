# Plan de validación — Presentaciones y carruseles

## Modelo de datos
Diapositiva, imagen, texto, enlace, orden.

## Implementación esperada
Preferir una única imagen potente; si no, desplazamiento CSS con controles de teclado, pausa y ninguna reproducción automática impuesta.

## Tests que deben preverse
1. Nominal: Navegar con el teclado y con lector de pantalla, medir el desplazamiento del diseño.
2. Control de rechazo: Sin JavaScript, todo el contenido de las diapositivas sigue siendo legible.
3. Invariante: Ninguna biblioteca de terceros pesada; respeto de prefers-reduced-motion.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
