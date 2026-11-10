# Plan de validación — Flujo de traducción

## Modelo de datos
Contenido de origen, versión de destino, traductor, estado, fecha de actualización.

## Implementación esperada
Llevar una tabla de los contenidos por traducir, producir las traducciones como borrador, hacerlas revisar por un hablante del idioma, señalar las versiones obsoletas.

## Tests que deben preverse
1. Nominal: Traducir una página, hacerla revisar, publicar y después modificar el origen y comprobar el aviso.
2. Control de rechazo: Una traducción no revisada permanece como borrador.
3. Invariante: Ninguna traducción jurídica o médica se publica sin una validación cualificada.
4. GET/HEAD: caché pública únicamente sin estado de sesión ni datos sensibles; canonical, estado HTTP, SEO y GEO sin cambios o mejorados.
5. POST: nunca caché compartida; CSRF, TLS, permisos, limitación de intentos, idempotencia. No ejecutar si el núcleo no lo soporta oficialmente.
6. Activación y desactivación: los contenidos se conservan y las rutas públicas se retiran sin fugas.
7. Controles: validador nativo, tests PHP y HTTP, presupuestos; registrar los comandos ejecutados, sus resultados y lo que no se ha probado.

## Prueba de disponibilidad
Estado de la función o de la extensión, registros de CI, matriz de tests, procedimiento de reversión y rechazo de toda promesa no verificada.
