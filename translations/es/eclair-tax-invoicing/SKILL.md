---
name: eclair-tax-invoicing
description: "Preparar los puntos de IVA y facturación adaptados a cada jurisdicción (sin tipo universal). Use on Éclair CMS 2.x when the user wants to: construir los puntos de conexión fiscales adaptados a la jurisdicción. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# IVA y facturación — Éclair CMS 2.x

## Desencadenante y resultado esperado
Utilizar este skill para **construir los puntos de conexión fiscales adaptados a la jurisdicción**. Esta función **exige capacidades ausentes del núcleo 2.0**: el skill entrega diseño, maqueta segura y tests, no una puesta en producción. Este skill es un **flujo de trabajo de agente**, no una extensión PHP funcional ni una garantía de conformidad.

**Equivalente en WordPress:** Impuestos de WooCommerce, plugins de facturas PDF. Familia: Commerce Pro.

## Diagnóstico obligatorio antes de cualquier modificación
1. Leer `references/core-map.md` (lo que el núcleo ya hace) y `references/native-contract.md`; comprobar la versión real del CMS y las capacidades en `GET /<admin>/api/capabilities` (si el acceso está autorizado).
2. Leer `references/family-contract.md` y `references/acceptance.md`. No copiar nunca el antiguo sistema de packs v0.x ni código PHP de WordPress en Éclair 2.
3. Identificar el modelo de datos: **País de venta y de entrega, localización fiscal, tipo impositivo vigente, factura, factura rectificativa, secuencia**. Documentar qué es público, qué es privado y de dónde procede cada dato.

## Procedimiento específico
4. **Recorrido:** Enumerar las jurisdicciones y los tipos de clientes; consultar las normas actualizadas y el asesoramiento contable; fijar la base imponible/el tipo en el momento del pedido; preparar exportaciones de facturas y facturas rectificativas. Describir los estados y los errores antes de escribir código.
5. **Ubicaciones:** código propio del sitio en `site/extensions/<id>/`, apariencia en `site/themes/<id>/`, datos bajo `$ctx['data']`, contenidos y ajustes mediante la administración o el MCP. No editar nunca `app/`, `assets/`, `index.php` ni el updater.
6. **Contrato actual:** El núcleo ya proporciona una tienda ligera (fichas de producto, variantes, categorías, enlaces de pago de un proveedor, feed de comerciante): utilizarla primero, sin duplicarla. Más allá de eso, el carrito, los pedidos y los pagos necesitan POST públicos, un almacenamiento transaccional fiable, webhooks autenticados e idempotencia; Éclair 2.0 oficial no proporciona todo eso. La PR #19 sigue siendo un borrador: no utilizar nunca una ruta POST no fusionada como prueba de compatibilidad.
7. **Invariante de seguridad:** No aplicar nunca un tipo de IVA universal ni pretender garantizar la conformidad fiscal sin validación local. Comprobar también los permisos en el servidor, el escapado con `e()`, la validación de los datos y la ausencia de secretos o de datos personales en el HTML público o en una caché compartida.
8. **Pruebas:** escribir el test positivo «Probar venta nacional, transfronteriza, reembolso y cambio de tipo impositivo» y el test de rechazo «Una factura emitida y después anulada no debe borrarse ni renumerarse silenciosamente». Medir las regresiones de SEO y de rendimiento, documentar la reversión.
9. **Validación nativa:** `php tools/validate.php <dossier> --json`, `php tests/run.php` y `php tools/measure.php --check` sobre un checkout oficial para todo paquete producido. Para una parte no soportada por el núcleo, entregar una nota de brecha y un test bloqueante, nunca un éxito ficticio.

## Entregables obligatorios
- Miniespecificación: objetivo, usuarios, recorridos, estados, datos, mediciones.
- Matriz de autorizaciones y de caché: ruta, método, sesión, visibilidad, indexación.
- Expediente de diseño, maqueta GET segura si resulta útil, tests bloqueantes y solicitud de evolución del núcleo; **sin paquete de producción**.
- Tests de los casos positivos y de los rechazos, procedimiento de desactivación que conserva los datos, nota de compatibilidad.

## Criterios de aceptación
- Probar venta nacional, transfronteriza, reembolso y cambio de tipo impositivo.
- Una factura emitida y después anulada no debe borrarse ni renumerarse silenciosamente.
- Nada se publica, se activa ni se pone en producción sin una persona autorizada; no se promete ninguna puntuación, posición ni cita por parte de una IA.
- Las partes no soportadas por Éclair 2.0 se señalan explícitamente como **no entregables en producción**.

**Estado de madurez de este skill:** `design-workflow-requires-verified-core-capabilities`. Ver `references/acceptance.md` para los casos de prueba reproducibles.
