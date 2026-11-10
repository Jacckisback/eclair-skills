# Plan de validación — Galerías de imágenes

## Modelo de datos
Galería, imágenes, leyendas, orden.

## Implementación esperada
Componer la galería en cuadrícula CSS a partir de las imágenes de la biblioteca de medios, con leyendas y textos alternativos.

## Tests que deben preverse
1. Nominal: Mostrar una galería de veinte imágenes en móvil y medir su peso.
2. Control de rechazo: Una imagen retirada de la biblioteca de medios no deja una miniatura rota.
3. Invariante: Ninguna imagen se carga desde un dominio de terceros.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
