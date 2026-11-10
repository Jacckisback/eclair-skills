---
name: eclair-wp-plugin-porting
description: "Sustituir un plugin de WordPress por su equivalente en Éclair. Use on Éclair CMS 2.x when the user wants to: sustituir una extensión de WordPress por su equivalente Éclair. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Portabilidad de extensiones de WordPress — Éclair CMS 2.x

## Desencadenante y resultado esperado
Utilizar este skill para **sustituir una extensión de WordPress por su equivalente Éclair**. Esta función es **realizable hoy** con el contrato nativo (tema, bloques, rutas GET, páginas de administración, tareas). Este skill es un **flujo de trabajo de agente**, no una extensión PHP funcional ni una garantía de conformidad.

**Equivalente en WordPress:** Cualquier extensión de WordPress que haya que sustituir. Familia: Desarrollo y herramientas.

## Diagnóstico obligatorio antes de cualquier modificación
1. Leer `references/core-map.md` (lo que el núcleo ya hace) y `references/native-contract.md`; comprobar la versión real del CMS y las capacidades en `GET /<admin>/api/capabilities` (si el acceso está autorizado).
2. Leer `references/family-contract.md` y `references/acceptance.md`. No copiar nunca el antiguo sistema de packs v0.x ni código PHP de WordPress en Éclair 2.
3. Identificar el modelo de datos: **Extensión de origen, funciones realmente utilizadas, equivalente nativo, diferencia**. Documentar qué es público, qué es privado y de dónde procede cada dato.

## Procedimiento específico
4. **Recorrido:** Enumerar lo que la extensión hace realmente en el sitio, buscar primero la función nativa, si no el skill del catálogo, si no una extensión a medida; no copiar nunca código PHP de WordPress. Describir los estados y los errores antes de escribir código.
5. **Ubicaciones:** código propio del sitio en `site/extensions/<id>/`, apariencia en `site/themes/<id>/`, datos bajo `$ctx['data']`, contenidos y ajustes mediante la administración o el MCP. No editar nunca `app/`, `assets/`, `index.php` ni el updater.
6. **Contrato actual:** Realizable con `eclair-extension/1` y el contrato de tema: rutas GET públicas cacheables, páginas de administración protegidas, bloques y ajustes declarativos, tareas programadas, recursos. Comprobar primero que no basta con un bloque o un ajuste nativo.
7. **Invariante de seguridad:** No se reutiliza ningún código con licencia incompatible o dependiente de la API de WordPress. Comprobar también los permisos en el servidor, el escapado con `e()`, la validación de los datos y la ausencia de secretos o de datos personales en el HTML público o en una caché compartida.
8. **Pruebas:** escribir el test positivo «Elaborar la tabla de correspondencias de un sitio real y hacerla validar» y el test de rechazo «Una función sin equivalente se anuncia como ausente, no se simula». Medir las regresiones de SEO y de rendimiento, documentar la reversión.
9. **Validación nativa:** `php tools/validate.php <dossier> --json`, `php tests/run.php` y `php tools/measure.php --check` sobre un checkout oficial para todo paquete producido. Para una parte no soportada por el núcleo, entregar una nota de brecha y un test bloqueante, nunca un éxito ficticio.

## Entregables obligatorios
- Miniespecificación: objetivo, usuarios, recorridos, estados, datos, mediciones.
- Matriz de autorizaciones y de caché: ruta, método, sesión, visibilidad, indexación.
- Paquete `extension.json`/`extension.php` o paquete de tema validado, solo si no basta con un bloque o un ajuste nativo.
- Tests de los casos positivos y de los rechazos, procedimiento de desactivación que conserva los datos, nota de compatibilidad.

## Criterios de aceptación
- Elaborar la tabla de correspondencias de un sitio real y hacerla validar.
- Una función sin equivalente se anuncia como ausente, no se simula.
- Nada se publica, se activa ni se pone en producción sin una persona autorizada; no se promete ninguna puntuación, posición ni cita por parte de una IA.
- Las partes no soportadas por Éclair 2.0 se señalan explícitamente como **no entregables en producción**.

**Estado de madurez de este skill:** `native-v2-workflow`. Ver `references/acceptance.md` para los casos de prueba reproducibles.
