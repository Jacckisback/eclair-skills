---
name: eclair-theme-builder
description: "Producir un tema Éclair v2 compatible con las actualizaciones. Use on Éclair CMS 2.x when the user wants to: producir un tema Éclair v2 compatible con las actualizaciones. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Creación de temas — Éclair CMS 2.x

## Desencadenante y resultado esperado
Utilizar este skill para **producir un tema Éclair v2 compatible con las actualizaciones**. Esta función es **realizable hoy** con el contrato nativo (tema, bloques, rutas GET, páginas de administración, tareas). Este skill es un **flujo de trabajo de agente**, no una extensión PHP funcional ni una garantía de conformidad.

**Equivalente en WordPress:** Temas hijo y temas de bloques. Familia: Diseño y UX.

## Diagnóstico obligatorio antes de cualquier modificación
1. Leer `references/core-map.md` (lo que el núcleo ya hace) y `references/native-contract.md`; comprobar la versión real del CMS y las capacidades en `GET /<admin>/api/capabilities` (si el acceso está autorizado).
2. Leer `references/family-contract.md` y `references/acceptance.md`. No copiar nunca el antiguo sistema de packs v0.x ni código PHP de WordPress en Éclair 2.
3. Identificar el modelo de datos: **theme.json, estilos, assets, templates declarados, licencia y procedencia**. Documentar qué es público, qué es privado y de dónde procede cada dato.

## Procedimiento específico
4. **Recorrido:** Partir del tema de ejemplo oficial, emplear las variables y plantillas admitidas, probar la preview y después el ZIP, comprobar la compatibilidad de versión. Describir los estados y los errores antes de escribir código.
5. **Ubicaciones:** código propio del sitio en `site/extensions/<id>/`, apariencia en `site/themes/<id>/`, datos bajo `$ctx['data']`, contenidos y ajustes mediante la administración o el MCP. No editar nunca `app/`, `assets/`, `index.php` ni el updater.
6. **Contrato actual:** Éclair v2 expone temas bajo site/themes y bloques declarativos de extensión. No modificar ni app/, ni index.php, ni la CSP, ni la generación de la caché; validar los temas mediante tools/validate.php.
7. **Invariante de seguridad:** No rehacer nunca el SEO head ni el canonical ni tocar los archivos del núcleo. Comprobar también los permisos en el servidor, el escapado con `e()`, la validación de los datos y la ausencia de secretos o de datos personales en el HTML público o en una caché compartida.
8. **Pruebas:** escribir el test positivo «Probar el validador de temas, la activación, la previsualización y la vuelta atrás» y el test de rechazo «Un template defectuoso no deja el sitio inaccesible gracias a la alternativa prevista». Medir las regresiones de SEO y de rendimiento, documentar la reversión.
9. **Validación nativa:** `php tools/validate.php <dossier> --json`, `php tests/run.php` y `php tools/measure.php --check` sobre un checkout oficial para todo paquete producido. Para una parte no soportada por el núcleo, entregar una nota de brecha y un test bloqueante, nunca un éxito ficticio.

## Entregables obligatorios
- Miniespecificación: objetivo, usuarios, recorridos, estados, datos, mediciones.
- Matriz de autorizaciones y de caché: ruta, método, sesión, visibilidad, indexación.
- Paquete `extension.json`/`extension.php` o paquete de tema validado, solo si no basta con un bloque o un ajuste nativo.
- Tests de los casos positivos y de los rechazos, procedimiento de desactivación que conserva los datos, nota de compatibilidad.

## Criterios de aceptación
- Probar el validador de temas, la activación, la previsualización y la vuelta atrás.
- Un template defectuoso no deja el sitio inaccesible gracias a la alternativa prevista.
- Nada se publica, se activa ni se pone en producción sin una persona autorizada; no se promete ninguna puntuación, posición ni cita por parte de una IA.
- Las partes no soportadas por Éclair 2.0 se señalan explícitamente como **no entregables en producción**.

**Estado de madurez de este skill:** `native-v2-workflow`. Ver `references/acceptance.md` para los casos de prueba reproducibles.
