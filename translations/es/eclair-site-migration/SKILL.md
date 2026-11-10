---
name: eclair-site-migration
description: "Trasladar un sitio Éclair sin perder contenidos ni posicionamiento. Use on Éclair CMS 2.x when the user wants to: trasladar un sitio Éclair sin pérdida de contenidos ni de posicionamiento. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Cambio de alojamiento o de dominio — Éclair CMS 2.x

## Desencadenante y resultado esperado
Utilizar este skill para **trasladar un sitio Éclair sin pérdida de contenidos ni de posicionamiento**. Esta función está **ya integrada en el núcleo de Éclair 2.0**: el skill guía su configuración y su verificación, sin escribir ninguna extensión. Este skill es un **flujo de trabajo de agente**, no una extensión PHP funcional ni una garantía de conformidad.

**Equivalente en WordPress:** Duplicator, All-in-One WP Migration. Familia: Administración y mantenimiento.

## Diagnóstico obligatorio antes de cualquier modificación
1. Leer `references/core-map.md` (lo que el núcleo ya hace) y `references/native-contract.md`; comprobar la versión real del CMS y las capacidades en `GET /<admin>/api/capabilities` (si el acceso está autorizado).
2. Leer `references/family-contract.md` y `references/acceptance.md`. No copiar nunca el antiguo sistema de packs v0.x ni código PHP de WordPress en Éclair 2.
3. Identificar el modelo de datos: **Copia de seguridad, nuevo alojamiento, DNS, redirecciones de dominio**. Documentar qué es público, qué es privado y de dónde procede cada dato.

## Procedimiento específico
4. **Recorrido:** Hacer una copia de seguridad, restaurar en el nuevo proveedor de alojamiento, verificar, cambiar el DNS, redirigir el dominio antiguo página a página. Describir los estados y los errores antes de escribir código.
5. **Ubicaciones:** código propio del sitio en `site/extensions/<id>/`, apariencia en `site/themes/<id>/`, datos bajo `$ctx['data']`, contenidos y ajustes mediante la administración o el MCP. No editar nunca `app/`, `assets/`, `index.php` ni el updater.
6. **Contrato actual:** La función existe en el núcleo: ajustarla mediante la administración o, en borrador, mediante el conector MCP. No duplicarla en una extensión y no modificar nunca el núcleo para adaptarla; si una necesidad supera lo que ofrece el núcleo, señalarla como una brecha.
7. **Invariante de seguridad:** Los secretos del sitio nunca viajan por correo electrónico ni por mensajería. Comprobar también los permisos en el servidor, el escapado con `e()`, la validación de los datos y la ausencia de secretos o de datos personales en el HTML público o en una caché compartida.
8. **Pruebas:** escribir el test positivo «Ensayar el traslado en un dominio de prueba» y el test de rechazo «Ninguna dirección antigua responde con un 404 tras el cambio». Medir las regresiones de SEO y de rendimiento, documentar la reversión.
9. **Validación nativa:** `php tools/validate.php <dossier> --json`, `php tests/run.php` y `php tools/measure.php --check` sobre un checkout oficial para todo paquete producido. Para una parte no soportada por el núcleo, entregar una nota de brecha y un test bloqueante, nunca un éxito ficticio.

## Entregables obligatorios
- Miniespecificación: objetivo, usuarios, recorridos, estados, datos, mediciones.
- Matriz de autorizaciones y de caché: ruta, método, sesión, visibilidad, indexación.
- Ajustes y contenidos preparados mediante la administración o en borrador mediante el MCP; **ninguna extensión** mientras lo nativo sea suficiente.
- Tests de los casos positivos y de los rechazos, procedimiento de desactivación que conserva los datos, nota de compatibilidad.

## Criterios de aceptación
- Ensayar el traslado en un dominio de prueba.
- Ninguna dirección antigua responde con un 404 tras el cambio.
- Nada se publica, se activa ni se pone en producción sin una persona autorizada; no se promete ninguna puntuación, posición ni cita por parte de una IA.
- Las partes no soportadas por Éclair 2.0 se señalan explícitamente como **no entregables en producción**.

**Estado de madurez de este skill:** `core-builtin-configuration-workflow`. Ver `references/acceptance.md` para los casos de prueba reproducibles.
