---
name: eclair-automation-platforms
description: "Conectar el sitio a Make, Zapier o n8n. Use on Éclair CMS 2.x when the user wants to: conectar el sitio con Make, Zapier o n8n. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Plataformas de automatización — Éclair CMS 2.x

## Desencadenante y resultado esperado
Utilizar este skill para **conectar el sitio con Make, Zapier o n8n**. La **parte pública de lectura es realizable hoy**; las escrituras por parte de los visitantes requieren más de lo que ofrece el contrato actual. Este skill es un **flujo de trabajo de agente**, no una extensión PHP funcional ni una garantía de conformidad.

**Equivalente en WordPress:** Zapier for WordPress, Uncanny Automator. Familia: Integraciones y automatización.

## Diagnóstico obligatorio antes de cualquier modificación
1. Leer `references/core-map.md` (lo que el núcleo ya hace) y `references/native-contract.md`; comprobar la versión real del CMS y las capacidades en `GET /<admin>/api/capabilities` (si el acceso está autorizado).
2. Leer `references/family-contract.md` y `references/acceptance.md`. No copiar nunca el antiguo sistema de packs v0.x ni código PHP de WordPress en Éclair 2.
3. Identificar el modelo de datos: **Escenario, activador, datos transmitidos**. Documentar qué es público, qué es privado y de dónde procede cada dato.

## Procedimiento específico
4. **Recorrido:** Exponer en lectura lo que la plataforma puede consultar (feeds, JSON público); diseñar la recepción de eventos para más adelante. Describir los estados y los errores antes de escribir código.
5. **Ubicaciones:** código propio del sitio en `site/extensions/<id>/`, apariencia en `site/themes/<id>/`, datos bajo `$ctx['data']`, contenidos y ajustes mediante la administración o el MCP. No editar nunca `app/`, `assets/`, `index.php` ni el updater.
6. **Contrato actual:** La lectura pública (GET, cacheable) es realizable hoy. Toda escritura por parte de un visitante exige una ruta POST pública que el núcleo 2.0 no abre a las extensiones (PR #19 en borrador, no fusionada): no simularla.
7. **Invariante de seguridad:** Ningún dato personal se expone en un punto de acceso público para facilitar una automatización. Comprobar también los permisos en el servidor, el escapado con `e()`, la validación de los datos y la ausencia de secretos o de datos personales en el HTML público o en una caché compartida.
8. **Pruebas:** escribir el test positivo «Hacer que la plataforma lea un feed público y active un escenario» y el test de rechazo «Una llamada entrante no autenticada no modifica nada en el sitio». Medir las regresiones de SEO y de rendimiento, documentar la reversión.
9. **Validación nativa:** `php tools/validate.php <dossier> --json`, `php tests/run.php` y `php tools/measure.php --check` sobre un checkout oficial para todo paquete producido. Para una parte no soportada por el núcleo, entregar una nota de brecha y un test bloqueante, nunca un éxito ficticio.

## Entregables obligatorios
- Miniespecificación: objetivo, usuarios, recorridos, estados, datos, mediciones.
- Matriz de autorizaciones y de caché: ruta, método, sesión, visibilidad, indexación.
- Paquete de solo lectura (rutas GET) validado, y plan escrito para la parte de escritura, claramente marcada como no entregada.
- Tests de los casos positivos y de los rechazos, procedimiento de desactivación que conserva los datos, nota de compatibilidad.

## Criterios de aceptación
- Hacer que la plataforma lea un feed público y active un escenario.
- Una llamada entrante no autenticada no modifica nada en el sitio.
- Nada se publica, se activa ni se pone en producción sin una persona autorizada; no se promete ninguna puntuación, posición ni cita por parte de una IA.
- Las partes no soportadas por Éclair 2.0 se señalan explícitamente como **no entregables en producción**.

**Estado de madurez de este skill:** `public-read-only-prototype-possible`. Ver `references/acceptance.md` para los casos de prueba reproducibles.
