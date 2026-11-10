---
name: eclair-appointments-calendar
description: "Gestionar citas e integrar calendarios externos. Use on Éclair CMS 2.x when the user wants to: concertar citas e integrar calendarios externos. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Citas y calendario — Éclair CMS 2.x

## Desencadenante y resultado esperado
Utilizar este skill para **concertar citas e integrar calendarios externos**. Esta función **exige capacidades ausentes del núcleo 2.0**: el skill entrega diseño, maqueta segura y tests, no una puesta en producción. Este skill es un **flujo de trabajo de agente**, no una extensión PHP funcional ni una garantía de conformidad.

**Equivalente en WordPress:** Amelia, Bookly, Simply Schedule Appointments. Familia: Aplicaciones de negocio.

## Diagnóstico obligatorio antes de cualquier modificación
1. Leer `references/core-map.md` (lo que el núcleo ya hace) y `references/native-contract.md`; comprobar la versión real del CMS y las capacidades en `GET /<admin>/api/capabilities` (si el acceso está autorizado).
2. Leer `references/family-contract.md` y `references/acceptance.md`. No copiar nunca el antiguo sistema de packs v0.x ni código PHP de WordPress en Éclair 2.
3. Identificar el modelo de datos: **Profesional, servicio, duración, márgenes (buffers), excepciones, eventos y zonas horarias**. Documentar qué es público, qué es privado y de dónde procede cada dato.

## Procedimiento específico
4. **Recorrido:** Normalizar los horarios en UTC, conservar la zona horaria de visualización, bloquear las franjas de indisponibilidad, gestionar la resincronización externa. Describir los estados y los errores antes de escribir código.
5. **Ubicaciones:** código propio del sitio en `site/extensions/<id>/`, apariencia en `site/themes/<id>/`, datos bajo `$ctx['data']`, contenidos y ajustes mediante la administración o el MCP. No editar nunca `app/`, `assets/`, `index.php` ni el updater.
6. **Contrato actual:** Los escaparates públicos son posibles con GET; las reservas, los pagos, las candidaturas, el CRM y los datos personales exigen POST seguro, un almacenamiento adecuado y permisos comprobados en el servidor.
7. **Invariante de seguridad:** Una integración externa requiere OAuth/scopes mínimos y no debe exponer los calendarios privados. Comprobar también los permisos en el servidor, el escapado con `e()`, la validación de los datos y la ausencia de secretos o de datos personales en el HTML público o en una caché compartida.
8. **Pruebas:** escribir el test positivo «Probar DST, cita que cruza la medianoche, evento eliminado» y el test de rechazo «Una franja bloqueada manualmente nunca se ofrece tras la resincronización». Medir las regresiones de SEO y de rendimiento, documentar la reversión.
9. **Validación nativa:** `php tools/validate.php <dossier> --json`, `php tests/run.php` y `php tools/measure.php --check` sobre un checkout oficial para todo paquete producido. Para una parte no soportada por el núcleo, entregar una nota de brecha y un test bloqueante, nunca un éxito ficticio.

## Entregables obligatorios
- Miniespecificación: objetivo, usuarios, recorridos, estados, datos, mediciones.
- Matriz de autorizaciones y de caché: ruta, método, sesión, visibilidad, indexación.
- Expediente de diseño, maqueta GET segura si resulta útil, tests bloqueantes y solicitud de evolución del núcleo; **sin paquete de producción**.
- Tests de los casos positivos y de los rechazos, procedimiento de desactivación que conserva los datos, nota de compatibilidad.

## Criterios de aceptación
- Probar DST, cita que cruza la medianoche, evento eliminado.
- Una franja bloqueada manualmente nunca se ofrece tras la resincronización.
- Nada se publica, se activa ni se pone en producción sin una persona autorizada; no se promete ninguna puntuación, posición ni cita por parte de una IA.
- Las partes no soportadas por Éclair 2.0 se señalan explícitamente como **no entregables en producción**.

**Estado de madurez de este skill:** `design-workflow-requires-verified-core-capabilities`. Ver `references/acceptance.md` para los casos de prueba reproducibles.
