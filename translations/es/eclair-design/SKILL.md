---
name: eclair-design
description: "Dirección de arte: crear sitios coherentes con Éclair Design y el tema nativo. Use on Éclair CMS 2.x when the user wants to: crear sitios coherentes con Éclair Design y el tema nativo. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Dirección artística Éclair — Éclair CMS 2.x

## Desencadenante y resultado esperado
Utilizar este skill para **crear sitios coherentes con Éclair Design y el tema nativo**. Esta función es **realizable hoy** con el contrato nativo (tema, bloques, rutas GET, páginas de administración, tareas). Este skill es un **flujo de trabajo de agente**, no una extensión PHP funcional ni una garantía de conformidad.

**Equivalente en WordPress:** Temas y personalizador de WordPress. Familia: Diseño y UX.

## Diagnóstico obligatorio antes de cualquier modificación
1. Leer `references/core-map.md` (lo que el núcleo ya hace) y `references/native-contract.md`; comprobar la versión real del CMS y las capacidades en `GET /<admin>/api/capabilities` (si el acceso está autorizado).
2. Leer `references/family-contract.md` y `references/acceptance.md`. No copiar nunca el antiguo sistema de packs v0.x ni código PHP de WordPress en Éclair 2.
3. Identificar el modelo de datos: **Posicionamiento, identidad, tipografía, colores, componentes, fotografías y contenido real**. Documentar qué es público, qué es privado y de dónde procede cada dato.

## Procedimiento específico
4. **Recorrido:** Definir un universo inspirado en la actividad del cliente, componer secciones, ajustar el CSS y probar los temas con contenido real; dar prioridad a site/themes y a los bloques existentes. Describir los estados y los errores antes de escribir código.
5. **Ubicaciones:** código propio del sitio en `site/extensions/<id>/`, apariencia en `site/themes/<id>/`, datos bajo `$ctx['data']`, contenidos y ajustes mediante la administración o el MCP. No editar nunca `app/`, `assets/`, `index.php` ni el updater.
6. **Contrato actual:** Éclair v2 expone temas bajo site/themes y bloques declarativos de extensión. No modificar ni app/, ni index.php, ni la CSP, ni la generación de la caché; validar los temas mediante tools/validate.php.
7. **Invariante de seguridad:** No modificar nunca app/theme/ ni romper el SEO, la CSP o la ruta rápida. Comprobar también los permisos en el servidor, el escapado con `e()`, la validación de los datos y la ausencia de secretos o de datos personales en el HTML público o en una caché compartida.
8. **Pruebas:** escribir el test positivo «Probar el contraste, la coherencia entre páginas y las versiones móviles» y el test de rechazo «La nueva apariencia sigue siendo legible sin JavaScript y respeta los enlaces existentes». Medir las regresiones de SEO y de rendimiento, documentar la reversión.
9. **Validación nativa:** `php tools/validate.php <dossier> --json`, `php tests/run.php` y `php tools/measure.php --check` sobre un checkout oficial para todo paquete producido. Para una parte no soportada por el núcleo, entregar una nota de brecha y un test bloqueante, nunca un éxito ficticio.

## Entregables obligatorios
- Miniespecificación: objetivo, usuarios, recorridos, estados, datos, mediciones.
- Matriz de autorizaciones y de caché: ruta, método, sesión, visibilidad, indexación.
- Paquete `extension.json`/`extension.php` o paquete de tema validado, solo si no basta con un bloque o un ajuste nativo.
- Tests de los casos positivos y de los rechazos, procedimiento de desactivación que conserva los datos, nota de compatibilidad.

## Criterios de aceptación
- Probar el contraste, la coherencia entre páginas y las versiones móviles.
- La nueva apariencia sigue siendo legible sin JavaScript y respeta los enlaces existentes.
- Nada se publica, se activa ni se pone en producción sin una persona autorizada; no se promete ninguna puntuación, posición ni cita por parte de una IA.
- Las partes no soportadas por Éclair 2.0 se señalan explícitamente como **no entregables en producción**.

**Estado de madurez de este skill:** `native-v2-workflow`. Ver `references/acceptance.md` para los casos de prueba reproducibles.
