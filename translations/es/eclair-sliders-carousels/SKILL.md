---
name: eclair-sliders-carousels
description: "Crear un carrusel sobrio que no perjudique la velocidad ni la accesibilidad. Use on Éclair CMS 2.x when the user wants to: crear una presentación de diapositivas sobria que no degrade ni la velocidad ni la accesibilidad. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Presentaciones y carruseles — Éclair CMS 2.x

## Desencadenante y resultado esperado
Utilizar este skill para **crear una presentación de diapositivas sobria que no degrade ni la velocidad ni la accesibilidad**. Esta función es **realizable hoy** con el contrato nativo (tema, bloques, rutas GET, páginas de administración, tareas). Este skill es un **flujo de trabajo de agente**, no una extensión PHP funcional ni una garantía de conformidad.

**Equivalente en WordPress:** Slider Revolution, Smart Slider, MetaSlider. Familia: Medios.

## Diagnóstico obligatorio antes de cualquier modificación
1. Leer `references/core-map.md` (lo que el núcleo ya hace) y `references/native-contract.md`; comprobar la versión real del CMS y las capacidades en `GET /<admin>/api/capabilities` (si el acceso está autorizado).
2. Leer `references/family-contract.md` y `references/acceptance.md`. No copiar nunca el antiguo sistema de packs v0.x ni código PHP de WordPress en Éclair 2.
3. Identificar el modelo de datos: **Diapositiva, imagen, texto, enlace, orden**. Documentar qué es público, qué es privado y de dónde procede cada dato.

## Procedimiento específico
4. **Recorrido:** Preferir una única imagen potente; si no, desplazamiento CSS con controles de teclado, pausa y ninguna reproducción automática impuesta. Describir los estados y los errores antes de escribir código.
5. **Ubicaciones:** código propio del sitio en `site/extensions/<id>/`, apariencia en `site/themes/<id>/`, datos bajo `$ctx['data']`, contenidos y ajustes mediante la administración o el MCP. No editar nunca `app/`, `assets/`, `index.php` ni el updater.
6. **Contrato actual:** Realizable con `eclair-extension/1` y el contrato de tema: rutas GET públicas cacheables, páginas de administración protegidas, bloques y ajustes declarativos, tareas programadas, recursos. Comprobar primero que no basta con un bloque o un ajuste nativo.
7. **Invariante de seguridad:** Ninguna biblioteca de terceros pesada; respeto de prefers-reduced-motion. Comprobar también los permisos en el servidor, el escapado con `e()`, la validación de los datos y la ausencia de secretos o de datos personales en el HTML público o en una caché compartida.
8. **Pruebas:** escribir el test positivo «Navegar con el teclado y con lector de pantalla, medir el desplazamiento del diseño» y el test de rechazo «Sin JavaScript, todo el contenido de las diapositivas sigue siendo legible». Medir las regresiones de SEO y de rendimiento, documentar la reversión.
9. **Validación nativa:** `php tools/validate.php <dossier> --json`, `php tests/run.php` y `php tools/measure.php --check` sobre un checkout oficial para todo paquete producido. Para una parte no soportada por el núcleo, entregar una nota de brecha y un test bloqueante, nunca un éxito ficticio.

## Entregables obligatorios
- Miniespecificación: objetivo, usuarios, recorridos, estados, datos, mediciones.
- Matriz de autorizaciones y de caché: ruta, método, sesión, visibilidad, indexación.
- Paquete `extension.json`/`extension.php` o paquete de tema validado, solo si no basta con un bloque o un ajuste nativo.
- Tests de los casos positivos y de los rechazos, procedimiento de desactivación que conserva los datos, nota de compatibilidad.

## Criterios de aceptación
- Navegar con el teclado y con lector de pantalla, medir el desplazamiento del diseño.
- Sin JavaScript, todo el contenido de las diapositivas sigue siendo legible.
- Nada se publica, se activa ni se pone en producción sin una persona autorizada; no se promete ninguna puntuación, posición ni cita por parte de una IA.
- Las partes no soportadas por Éclair 2.0 se señalan explícitamente como **no entregables en producción**.

**Estado de madurez de este skill:** `native-v2-workflow`. Ver `references/acceptance.md` para los casos de prueba reproducibles.
