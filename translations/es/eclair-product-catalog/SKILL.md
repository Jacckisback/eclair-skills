---
name: eclair-product-catalog
description: "Crear un catálogo público de productos rápido e indexable. Use on Éclair CMS 2.x when the user wants to: construir un catálogo público rápido e indexable. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Catálogo de productos — Éclair CMS 2.x

## Desencadenante y resultado esperado
Utilizar este skill para **construir un catálogo público rápido e indexable**. Esta función está **ya integrada en el núcleo de Éclair 2.0**: el skill guía su configuración y su verificación, sin escribir ninguna extensión. Este skill es un **flujo de trabajo de agente**, no una extensión PHP funcional ni una garantía de conformidad.

**Equivalente en WordPress:** Catálogo de WooCommerce. Familia: Commerce Pro.

## Diagnóstico obligatorio antes de cualquier modificación
1. Leer `references/core-map.md` (lo que el núcleo ya hace) y `references/native-contract.md`; comprobar la versión real del CMS y las capacidades en `GET /<admin>/api/capabilities` (si el acceso está autorizado).
2. Leer `references/family-contract.md` y `references/acceptance.md`. No copiar nunca el antiguo sistema de packs v0.x ni código PHP de WordPress en Éclair 2.
3. Identificar el modelo de datos: **Producto, SKU, slug, título, descripción, precio de presentación, medio, disponibilidad y categoría**. Documentar qué es público, qué es privado y de dónde procede cada dato.

## Procedimiento específico
4. **Recorrido:** Prototipar primero una página pública GET cacheable; producir un esquema de producto y su índice; mantener los títulos y descripciones de origen; definir paginación y canonical; preservar los slugs a lo largo de las ediciones. Describir los estados y los errores antes de escribir código.
5. **Ubicaciones:** código propio del sitio en `site/extensions/<id>/`, apariencia en `site/themes/<id>/`, datos bajo `$ctx['data']`, contenidos y ajustes mediante la administración o el MCP. No editar nunca `app/`, `assets/`, `index.php` ni el updater.
6. **Contrato actual:** El núcleo ya proporciona una tienda ligera (fichas de producto, variantes, categorías, enlaces de pago de un proveedor, feed de comerciante): utilizarla primero, sin duplicarla. Más allá de eso, el carrito, los pedidos y los pagos necesitan POST públicos, un almacenamiento transaccional fiable, webhooks autenticados e idempotencia; Éclair 2.0 oficial no proporciona todo eso. La PR #19 sigue siendo un borrador: no utilizar nunca una ruta POST no fusionada como prueba de compatibilidad.
7. **Invariante de seguridad:** El precio mostrado nunca se toma como fuente de autoridad en un pedido futuro. Comprobar también los permisos en el servidor, el escapado con `e()`, la validación de los datos y la ausencia de secretos o de datos personales en el HTML público o en una caché compartida.
8. **Pruebas:** escribir el test positivo «Probar categorías, listados vacíos, URL canónica, búsqueda y eliminación soft» y el test de rechazo «Un producto eliminado o privado no debe permanecer en el catálogo ni en una caché antigua». Medir las regresiones de SEO y de rendimiento, documentar la reversión.
9. **Validación nativa:** `php tools/validate.php <dossier> --json`, `php tests/run.php` y `php tools/measure.php --check` sobre un checkout oficial para todo paquete producido. Para una parte no soportada por el núcleo, entregar una nota de brecha y un test bloqueante, nunca un éxito ficticio.

## Entregables obligatorios
- Miniespecificación: objetivo, usuarios, recorridos, estados, datos, mediciones.
- Matriz de autorizaciones y de caché: ruta, método, sesión, visibilidad, indexación.
- Ajustes y contenidos preparados mediante la administración o en borrador mediante el MCP; **ninguna extensión** mientras lo nativo sea suficiente.
- Tests de los casos positivos y de los rechazos, procedimiento de desactivación que conserva los datos, nota de compatibilidad.

## Criterios de aceptación
- Probar categorías, listados vacíos, URL canónica, búsqueda y eliminación soft.
- Un producto eliminado o privado no debe permanecer en el catálogo ni en una caché antigua.
- Nada se publica, se activa ni se pone en producción sin una persona autorizada; no se promete ninguna puntuación, posición ni cita por parte de una IA.
- Las partes no soportadas por Éclair 2.0 se señalan explícitamente como **no entregables en producción**.

**Estado de madurez de este skill:** `core-builtin-configuration-workflow`. Ver `references/acceptance.md` para los casos de prueba reproducibles.
