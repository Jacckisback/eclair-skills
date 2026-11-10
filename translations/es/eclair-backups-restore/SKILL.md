---
name: eclair-backups-restore
description: "Planificar las copias de seguridad nativas y demostrar que se sabe restaurar. Use on Éclair CMS 2.x when the user wants to: planificar las copias de seguridad nativas y demostrar que se sabe restaurar. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Copias de seguridad y restauración — Éclair CMS 2.x

## Desencadenante y resultado esperado
Utilizar este skill para **planificar las copias de seguridad nativas y demostrar que se sabe restaurar**. Esta función está **ya integrada en el núcleo de Éclair 2.0**: el skill guía su configuración y su verificación, sin escribir ninguna extensión. Este skill es un **flujo de trabajo de agente**, no una extensión PHP funcional ni una garantía de conformidad.

**Equivalente en WordPress:** UpdraftPlus, BackWPup, Duplicator. Familia: Administración y mantenimiento.

## Diagnóstico obligatorio antes de cualquier modificación
1. Leer `references/core-map.md` (lo que el núcleo ya hace) y `references/native-contract.md`; comprobar la versión real del CMS y las capacidades en `GET /<admin>/api/capabilities` (si el acceso está autorizado).
2. Leer `references/family-contract.md` y `references/acceptance.md`. No copiar nunca el antiguo sistema de packs v0.x ni código PHP de WordPress en Éclair 2.
3. Identificar el modelo de datos: **Archivo de copia de seguridad, fecha, destino, prueba de restauración**. Documentar qué es público, qué es privado y de dónde procede cada dato.

## Procedimiento específico
4. **Recorrido:** Activar la copia de seguridad descargable o hacia el almacenamiento remoto previsto por el núcleo, fijar la frecuencia, restaurar en una copia para verificar. Describir los estados y los errores antes de escribir código.
5. **Ubicaciones:** código propio del sitio en `site/extensions/<id>/`, apariencia en `site/themes/<id>/`, datos bajo `$ctx['data']`, contenidos y ajustes mediante la administración o el MCP. No editar nunca `app/`, `assets/`, `index.php` ni el updater.
6. **Contrato actual:** La función existe en el núcleo: ajustarla mediante la administración o, en borrador, mediante el conector MCP. No duplicarla en una extensión y no modificar nunca el núcleo para adaptarla; si una necesidad supera lo que ofrece el núcleo, señalarla como una brecha.
7. **Invariante de seguridad:** Una copia de seguridad contiene datos personales: se almacena cifrada o en lugar seguro, nunca en una carpeta pública. Comprobar también los permisos en el servidor, el escapado con `e()`, la validación de los datos y la ausencia de secretos o de datos personales en el HTML público o en una caché compartida.
8. **Pruebas:** escribir el test positivo «Restaurar la última copia de seguridad en una instalación de prueba y comparar» y el test de rechazo «Un archivo modificado o malicioso se rechaza en la restauración». Medir las regresiones de SEO y de rendimiento, documentar la reversión.
9. **Validación nativa:** `php tools/validate.php <dossier> --json`, `php tests/run.php` y `php tools/measure.php --check` sobre un checkout oficial para todo paquete producido. Para una parte no soportada por el núcleo, entregar una nota de brecha y un test bloqueante, nunca un éxito ficticio.

## Entregables obligatorios
- Miniespecificación: objetivo, usuarios, recorridos, estados, datos, mediciones.
- Matriz de autorizaciones y de caché: ruta, método, sesión, visibilidad, indexación.
- Ajustes y contenidos preparados mediante la administración o en borrador mediante el MCP; **ninguna extensión** mientras lo nativo sea suficiente.
- Tests de los casos positivos y de los rechazos, procedimiento de desactivación que conserva los datos, nota de compatibilidad.

## Criterios de aceptación
- Restaurar la última copia de seguridad en una instalación de prueba y comparar.
- Un archivo modificado o malicioso se rechaza en la restauración.
- Nada se publica, se activa ni se pone en producción sin una persona autorizada; no se promete ninguna puntuación, posición ni cita por parte de una IA.
- Las partes no soportadas por Éclair 2.0 se señalan explícitamente como **no entregables en producción**.

**Estado de madurez de este skill:** `core-builtin-configuration-workflow`. Ver `references/acceptance.md` para los casos de prueba reproducibles.
