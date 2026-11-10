---
name: eclair-architecture
description: Use for Éclair CMS v2 architecture decisions, reviewing system boundaries and choosing whether a feature belongs to native settings, a theme, an extension or an isolated core RFC.
---

# Éclair Architecture — preservar el núcleo v2

## Objetivo
Diseñar la solución solicitada **sin copiar un sistema de extensiones** y sin sobrecargar la ruta de caché. Empezar por `references/core-map.md` y el código del checkout actual.

## Desarrollo operativo
1. Anotar el commit, la versión `ECLAIR_VERSION`, PHP y las capacidades disponibles mediante `/admin/api/capabilities` si el acceso está autorizado.
2. Clasificar el objetivo: contenido/ajuste nativo, tema de sitio, extensión `eclair-extension/1`, servicio externo o carencia del contrato público que requiere una RFC.
3. Buscar primero `Extensions`, `Themes`, `Packages`, `Migrations`, `Store`, `Cache`, `Site`, `Seo`, `Security`, `Mcp` y los docs `docs/ARCHITECTURE-2.md`/`docs/STATUS-2.md`.
4. Describir las fronteras: código bajo `site/extensions/` o `site/themes/`, datos mediante `Store` y `$ctx['data']`, medios bajo `media/`, ningún reemplazo de `app/`.
5. Distinguir estrictamente el contrato nativo (`eclair-extension/1`) de los antiguos experimentos v0.8 (rutas/permisos/SQL/outbox), incompatibles con v2 sin portarlos.
6. Elaborar una decisión de arquitectura explícita: alternativas, límites de la API, riesgos, rollback, test de compatibilidad e indicadores de rendimiento.
7. Hacer revisar y después validar con `php tests/run.php`, `php tools/measure.php --check` y los tests pertinentes de `tests/extensions.php`.

## Innegociables
Preservar SEO/GEO, etiquetado canónico, protecciones CSRF/CSP, gestión de la autenticación y caché caliente. Una extensión no se activa nunca a sí misma. No pretender gestionar un checkout transaccional ni las cuentas de alumnos mientras esos contratos no estén implementados y probados.

## Entregables
ADR y cartografía antes/después, decisión «native / extension / core RFC», restricciones, tests y plan de reversión. La plantilla `assets/architecture-decision.md` puede servir de punto de partida.

## V1.0 — Extensiones de miembros
La extensión nativa `examples/extensions/member-directory` ilustra las cuentas públicas separadas: ningún rol nuevo en `Eclair\Users`. Un núcleo 2.0 recibe las extensiones mediante `site/extensions/<id>`; ninguna escritura en `app/`.

## Éclair 2.0 — prototipo v1.1 (experimental)
Éclair 2.0.0 dispone ahora de un contrato experimental de POST público únicamente si el patch v1.1 se aplica sobre una rama de desarrollo. El núcleo oficial **no** proporciona este contrato. Ninguna modificación directa del núcleo desde un skill; preparación de una RFC y tests previos.

## Éclair 2.0 — registro y recuperación (v1.2 experimental)

Leer `references/member-email-v1.2.md` antes de cualquier petición de creación de cuentas de clientes/alumnos o de recuperación de contraseña. El módulo `member-directory` v0.3 utiliza rutas públicas POST **fuera del contrato oficial**; no prometer nunca una instalación directa en un Éclair 2.0 sin modificar ni activar los flujos de email sin una URL HTTPS verificada y tests nativos. Preferir el sistema de extensiones v2 a cualquier modificación de la antigua arquitectura v0.x. Mantener separadas las cuentas públicas y las de administración, rechazar toda caché compartida para las páginas de miembros y tratar los emails como no entregados mientras no exista ninguna confirmación.
