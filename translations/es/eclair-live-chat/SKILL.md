---
name: eclair-live-chat
description: "Ofrecer contacto inmediato sin un widget pesado. Use on Éclair CMS 2.x when the user wants to: ofrecer un contacto inmediato sin un widget pesado. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Chat en directo — Éclair CMS 2.x

## Desencadenante y resultado esperado
Utilizar este skill para **ofrecer un contacto inmediato sin un widget pesado**. Esta función está **parcialmente bloqueada por el contrato del núcleo**: el skill entrega lo que es nativo y documenta la brecha. Este skill es un **flujo de trabajo de agente**, no una extensión PHP funcional ni una garantía de conformidad.

**Equivalente en WordPress:** Tidio, Crisp, tawk.to. Familia: Integraciones y automatización.

## Diagnóstico obligatorio antes de cualquier modificación
1. Leer `references/core-map.md` (lo que el núcleo ya hace) y `references/native-contract.md`; comprobar la versión real del CMS y las capacidades en `GET /<admin>/api/capabilities` (si el acceso está autorizado).
2. Leer `references/family-contract.md` y `references/acceptance.md`. No copiar nunca el antiguo sistema de packs v0.x ni código PHP de WordPress en Éclair 2.
3. Identificar el modelo de datos: **Canal, horario, enlace de conversación**. Documentar qué es público, qué es privado y de dónde procede cada dato.

## Procedimiento específico
4. **Recorrido:** Preferir un enlace a un servicio de mensajería (WhatsApp, correo electrónico, teléfono) con horario; un widget de terceros depende de la política de contenido nativa. Describir los estados y los errores antes de escribir código.
5. **Ubicaciones:** código propio del sitio en `site/extensions/<id>/`, apariencia en `site/themes/<id>/`, datos bajo `$ctx['data']`, contenidos y ajustes mediante la administración o el MCP. No editar nunca `app/`, `assets/`, `index.php` ni el updater.
6. **Contrato actual:** Una parte depende de un punto de enganche ausente del contrato 2.0 (tipos de contenido, contribución SEO o JSON-LD, política de contenido por extensión, filtro de renderizado). Entregar la parte nativa y documentar con precisión la brecha, sin rodeos para eludirla.
7. **Invariante de seguridad:** Ningún widget carga un rastreador antes de una acción del visitante. Comprobar también los permisos en el servidor, el escapado con `e()`, la validación de los datos y la ausencia de secretos o de datos personales en el HTML público o en una caché compartida.
8. **Pruebas:** escribir el test positivo «Abrir el canal desde móvil y ordenador» y el test de rechazo «Fuera de horario, el sitio lo anuncia en lugar de prometer una respuesta inmediata». Medir las regresiones de SEO y de rendimiento, documentar la reversión.
9. **Validación nativa:** `php tools/validate.php <dossier> --json`, `php tests/run.php` y `php tools/measure.php --check` sobre un checkout oficial para todo paquete producido. Para una parte no soportada por el núcleo, entregar una nota de brecha y un test bloqueante, nunca un éxito ficticio.

## Entregables obligatorios
- Miniespecificación: objetivo, usuarios, recorridos, estados, datos, mediciones.
- Matriz de autorizaciones y de caché: ruta, método, sesión, visibilidad, indexación.
- Paquete o ajustes para la parte nativa, y nota de brecha precisa para la parte bloqueada.
- Tests de los casos positivos y de los rechazos, procedimiento de desactivación que conserva los datos, nota de compatibilidad.

## Criterios de aceptación
- Abrir el canal desde móvil y ordenador.
- Fuera de horario, el sitio lo anuncia en lugar de prometer una respuesta inmediata.
- Nada se publica, se activa ni se pone en producción sin una persona autorizada; no se promete ninguna puntuación, posición ni cita por parte de una IA.
- Las partes no soportadas por Éclair 2.0 se señalan explícitamente como **no entregables en producción**.

**Estado de madurez de este skill:** `partly-blocked-by-core-contract`. Ver `references/acceptance.md` para los casos de prueba reproducibles.
