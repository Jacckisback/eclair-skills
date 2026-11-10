---
name: eclair-cache-contract
description: Use when deciding Éclair CMS v2 static/uncached extension route behavior, invalidation, privacy and performance budgets.
---

# Éclair Cache Contract — mantener la caché segura

## Decisión
1. Leer `eclair/index.php`, `Cache.php`, `Extensions::route()` y `docs/EXTENSION-CONTRACT.md` del núcleo v2 objetivo.
2. Para las páginas de extensión con contenido público idéntico para todos, `routes.public[].cache` puede ser `true` tras comprobar las dependencias de renderizado.
3. Para contenidos privados, estados de usuario, carritos, tokens o precios personalizados: **sin caché compartida** (`Cache-Control: private, no-store`), `noindex` pertinente y contrato de autenticación en el servidor. No pretender nunca que un `cache:false` implemente por sí solo la autenticación.
4. Medir GET/HEAD y query strings, primera generación y después caché HIT, edición de los datos, activación/desactivación y migraciones. Comprobar las rutas del CMS y el índice `data/ext-public.php`.
5. No añadir nunca un lookup ni una lectura de registro al camino rápido `index.php` sin un presupuesto medido y una justificación de seguridad.
6. Probar `php tools/measure.php --check` y los presupuestos de `tools/budgets.json`, y después comparar con un baseline limpio con la misma versión de PHP y los mismos datos.
7. Comprobar la purga tras la activación y que las páginas públicas no afectadas sigan siendo cacheables; probar cookies y cabeceras en situación de concurrencia.

## Entregables
Matriz URL × método × identidad × caché, mediciones y tests de aislamiento.

## V1.0 — Identidad y caché
No servir nunca una página personalizada a partir de una caché compartida. Las rutas de administrador existentes ya son `private, no-store`; las futuras páginas públicas de miembros necesitan un contrato de ruta privada antes de cualquier apertura. No suponer nunca que `cache:false` implementa automáticamente garantías completas de sesión/CSRF.

## Éclair 2.0 — prototipo v1.1 (experimental)
Los formularios públicos GET utilizan `Security::formField()` y deben declararse `cache:false`. Sus respuestas no deben alcanzar el fast path del núcleo. POST queda excluido del fast path y forzado a no-store. Probar la purga en la activación del módulo y comprobar la ausencia de cookies/identidades en el HTML de la caché compartida.

## Éclair 2.0 — registro y recuperación (v1.2 experimental)

Leer `references/member-email-v1.2.md` antes de cualquier petición de creación de cuentas de clientes/alumnos o de recuperación de contraseña. El módulo `member-directory` v0.3 utiliza rutas públicas POST **fuera del contrato oficial**; no prometer nunca una instalación directa en un Éclair 2.0 sin modificar ni activar los flujos de email sin una URL HTTPS verificada y tests nativos. Preferir el sistema de extensiones v2 a cualquier modificación de la antigua arquitectura v0.x. Mantener separadas las cuentas públicas y las de administración, rechazar toda caché compartida para las páginas de miembros y tratar los emails como no entregados mientras no exista ninguna confirmación.
