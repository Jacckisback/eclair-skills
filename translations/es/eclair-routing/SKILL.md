---
name: eclair-routing
description: Use when creating Éclair CMS 2.0 extension public/admin routes and maintaining exact URLs, redirects and WordPress SEO migration compatibility.
---

# Éclair Routing — proteger las URL y la compatibilidad

## Procedimiento
1. Anotar las rutas y los alias existentes, `Site.php`, `App.php`, `Aliases.php`, `Redirects.php`, `Content::byRoute` y las URL reservadas.
2. Las rutas públicas de extensión `routes.public[]` son **solo GET** y están enumeradas explícitamente. Nada de ruta genérica `/{slug}` mediante un manifiesto inventado.
3. Las rutas admin utilizan `routes.admin[]`, método GET/POST, bajo `/<admin>/x/<id>/...` y con el permiso `right` nativo.
4. Probar antes de la activación las colisiones con artículos/páginas/productos, rutas reservadas, slug multilingüe, sitio en subcarpeta y otras extensiones.
5. Preservar la ruta exacta de una migración de WordPress (barra final, .html, acentos) mediante los mecanismos v2 `route`/`Aliases`, sin crear varios canonicals ni cascadas de 301.
6. Para una función que requiera rutas públicas POST (checkout, API de cliente), documentar una RFC/nueva interfaz segura en lugar de interceptar el núcleo o de eludir el enrutador.
7. Comprobar canonicals, sitemap, JSON-LD, noindex para las interfaces privadas, `HEAD`, respuestas 404/405 y caché.

## Entregables
Tabla de rutas, propietario del namespace, plan de redirecciones, conflictos detectados y tests HTTP.

## V1.0 — Ruta pública de inicio de sesión prohibida
Los GET públicos declarativos de Éclair 2.0 son adecuados para páginas públicas, **no** para un formulario POST de inicio de sesión. No debe crearse con GET ninguna ruta `/login` ni `/register` con efectos secundarios. `member-directory` solo declara rutas admin con permiso `users`.

## Éclair 2.0 — prototipo v1.1 (experimental)
Las rutas públicas POST **no** están presentes en Éclair 2.0 oficial. El patch propuesto v1.1 hace una excepción controlada: método POST explícito, `cache:false`, HTTPS, `Security::checkFormToken()`, respuesta `private,no-store`, redirección 303 relativa. Realizar siempre pruebas HTTP con el CMS completo antes de la fusión.

## Éclair 2.0 — registro y recuperación (v1.2 experimental)

Leer `references/member-email-v1.2.md` antes de cualquier petición de creación de cuentas de clientes/alumnos o de recuperación de contraseña. El módulo `member-directory` v0.3 utiliza rutas públicas POST **fuera del contrato oficial**; no prometer nunca una instalación directa en un Éclair 2.0 sin modificar ni activar los flujos de email sin una URL HTTPS verificada y tests nativos. Preferir el sistema de extensiones v2 a cualquier modificación de la antigua arquitectura v0.x. Mantener separadas las cuentas públicas y las de administración, rechazar toda caché compartida para las páginas de miembros y tratar los emails como no entregados mientras no exista ninguna confirmación.
