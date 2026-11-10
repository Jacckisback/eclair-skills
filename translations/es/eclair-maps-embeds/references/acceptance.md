# Plan de validación — Mapas y planos de acceso

## Modelo de datos
Dirección, coordenadas, imagen de mapa, enlace de ruta.

## Implementación esperada
Preferir una imagen de mapa estática con enlace a la ruta; un mapa interactivo de terceros depende de la política de contenido nativa.

## Tests que deben preverse
1. Nominal: Verificar imagen, texto alternativo y enlace de ruta en móvil.
2. Control de rechazo: Ninguna petición a un servicio de mapas al cargar la página.
3. Invariante: Ningún mapa de terceros cargado antes de una acción del visitante.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
