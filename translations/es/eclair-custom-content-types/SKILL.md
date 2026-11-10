---
name: eclair-custom-content-types
description: "Modelar contenidos de negocio (proyectos, inmuebles, eventos) sin tipos de contenido personalizados en el núcleo. Use on Éclair CMS 2.x when the user wants to: modelar contenidos de negocio (proyectos realizados, inmuebles, eventos) sin tipo de contenido personalizado en el núcleo. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Tipos de contenido personalizados — Éclair CMS 2.x

## Desencadenante y resultado esperado
Utilizar este skill para **modelar contenidos de negocio (proyectos realizados, inmuebles, eventos) sin tipo de contenido personalizado en el núcleo**. Esta función está **parcialmente bloqueada por el contrato del núcleo**: el skill entrega lo que es nativo y documenta la brecha. Este skill es un **flujo de trabajo de agente**, no una extensión PHP funcional ni una garantía de conformidad.

**Equivalente en WordPress:** Custom Post Types (CPT UI, ACF). Familia: Contenido y edición.

## Diagnóstico obligatorio antes de cualquier modificación
1. Leer `references/core-map.md` (lo que el núcleo ya hace) y `references/native-contract.md`; comprobar la versión real del CMS y las capacidades en `GET /<admin>/api/capabilities` (si el acceso está autorizado).
2. Leer `references/family-contract.md` y `references/acceptance.md`. No copiar nunca el antiguo sistema de packs v0.x ni código PHP de WordPress en Éclair 2.
3. Identificar el modelo de datos: **Ficha de negocio, campos, listado, dirección, estado**. Documentar qué es público, qué es privado y de dónde procede cada dato.

## Procedimiento específico
4. **Recorrido:** Elegir entre páginas con bloques dedicados y una extensión con almacenamiento propio y rutas GET, fijar las direcciones, prever listado y ficha. Describir los estados y los errores antes de escribir código.
5. **Ubicaciones:** código propio del sitio en `site/extensions/<id>/`, apariencia en `site/themes/<id>/`, datos bajo `$ctx['data']`, contenidos y ajustes mediante la administración o el MCP. No editar nunca `app/`, `assets/`, `index.php` ni el updater.
6. **Contrato actual:** Una parte depende de un punto de enganche ausente del contrato 2.0 (tipos de contenido, contribución SEO o JSON-LD, política de contenido por extensión, filtro de renderizado). Entregar la parte nativa y documentar con precisión la brecha, sin rodeos para eludirla.
7. **Invariante de seguridad:** No escribir nunca en los archivos de contenidos del núcleo desde una extensión. Comprobar también los permisos en el servidor, el escapado con `e()`, la validación de los datos y la ausencia de secretos o de datos personales en el HTML público o en una caché compartida.
8. **Pruebas:** escribir el test positivo «Crear un tipo de ficha mediante una extensión, con listado y detalle en GET, y después validar el paquete» y el test de rechazo «Una ficha no publicada no se sirve ni en el listado ni por su dirección directa». Medir las regresiones de SEO y de rendimiento, documentar la reversión.
9. **Validación nativa:** `php tools/validate.php <dossier> --json`, `php tests/run.php` y `php tools/measure.php --check` sobre un checkout oficial para todo paquete producido. Para una parte no soportada por el núcleo, entregar una nota de brecha y un test bloqueante, nunca un éxito ficticio.

## Entregables obligatorios
- Miniespecificación: objetivo, usuarios, recorridos, estados, datos, mediciones.
- Matriz de autorizaciones y de caché: ruta, método, sesión, visibilidad, indexación.
- Paquete o ajustes para la parte nativa, y nota de brecha precisa para la parte bloqueada.
- Tests de los casos positivos y de los rechazos, procedimiento de desactivación que conserva los datos, nota de compatibilidad.

## Criterios de aceptación
- Crear un tipo de ficha mediante una extensión, con listado y detalle en GET, y después validar el paquete.
- Una ficha no publicada no se sirve ni en el listado ni por su dirección directa.
- Nada se publica, se activa ni se pone en producción sin una persona autorizada; no se promete ninguna puntuación, posición ni cita por parte de una IA.
- Las partes no soportadas por Éclair 2.0 se señalan explícitamente como **no entregables en producción**.

**Estado de madurez de este skill:** `partly-blocked-by-core-contract`. Ver `references/acceptance.md` para los casos de prueba reproducibles.
