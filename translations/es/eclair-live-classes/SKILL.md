---
name: eclair-live-classes
description: "Anunciar y organizar clases en directo por videoconferencia. Use on Éclair CMS 2.x when the user wants to: anunciar y organizar clases por videoconferencia. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Clases en directo — Éclair CMS 2.x

## Desencadenante y resultado esperado
Utilizar este skill para **anunciar y organizar clases por videoconferencia**. La **parte pública de lectura es realizable hoy**; las escrituras por parte de los visitantes requieren más de lo que ofrece el contrato actual. Este skill es un **flujo de trabajo de agente**, no una extensión PHP funcional ni una garantía de conformidad.

**Equivalente en WordPress:** Integraciones de Zoom de los LMS. Familia: LMS.

## Diagnóstico obligatorio antes de cualquier modificación
1. Leer `references/core-map.md` (lo que el núcleo ya hace) y `references/native-contract.md`; comprobar la versión real del CMS y las capacidades en `GET /<admin>/api/capabilities` (si el acceso está autorizado).
2. Leer `references/family-contract.md` y `references/acceptance.md`. No copiar nunca el antiguo sistema de packs v0.x ni código PHP de WordPress en Éclair 2.
3. Identificar el modelo de datos: **Sesión, fecha, zona horaria, enlace de conexión, inscritos**. Documentar qué es público, qué es privado y de dónde procede cada dato.

## Procedimiento específico
4. **Recorrido:** Publicar el calendario de sesiones en GET, enviar el enlace de conexión a través del servicio de videoconferencia o por correo electrónico, no en una página pública. Describir los estados y los errores antes de escribir código.
5. **Ubicaciones:** código propio del sitio en `site/extensions/<id>/`, apariencia en `site/themes/<id>/`, datos bajo `$ctx['data']`, contenidos y ajustes mediante la administración o el MCP. No editar nunca `app/`, `assets/`, `index.php` ni el updater.
6. **Contrato actual:** La lectura pública (GET, cacheable) es realizable hoy. Toda escritura por parte de un visitante exige una ruta POST pública que el núcleo 2.0 no abre a las extensiones (PR #19 en borrador, no fusionada): no simularla.
7. **Invariante de seguridad:** El enlace de una sesión de pago o privada nunca se publica. Comprobar también los permisos en el servidor, el escapado con `e()`, la validación de los datos y la ausencia de secretos o de datos personales en el HTML público o en una caché compartida.
8. **Pruebas:** escribir el test positivo «Verificar la visualización de las fechas en dos zonas horarias» y el test de rechazo «Una sesión pasada deja de ofrecerse para inscripción». Medir las regresiones de SEO y de rendimiento, documentar la reversión.
9. **Validación nativa:** `php tools/validate.php <dossier> --json`, `php tests/run.php` y `php tools/measure.php --check` sobre un checkout oficial para todo paquete producido. Para una parte no soportada por el núcleo, entregar una nota de brecha y un test bloqueante, nunca un éxito ficticio.

## Entregables obligatorios
- Miniespecificación: objetivo, usuarios, recorridos, estados, datos, mediciones.
- Matriz de autorizaciones y de caché: ruta, método, sesión, visibilidad, indexación.
- Paquete de solo lectura (rutas GET) validado, y plan escrito para la parte de escritura, claramente marcada como no entregada.
- Tests de los casos positivos y de los rechazos, procedimiento de desactivación que conserva los datos, nota de compatibilidad.

## Criterios de aceptación
- Verificar la visualización de las fechas en dos zonas horarias.
- Una sesión pasada deja de ofrecerse para inscripción.
- Nada se publica, se activa ni se pone en producción sin una persona autorizada; no se promete ninguna puntuación, posición ni cita por parte de una IA.
- Las partes no soportadas por Éclair 2.0 se señalan explícitamente como **no entregables en producción**.

**Estado de madurez de este skill:** `public-read-only-prototype-possible`. Ver `references/acceptance.md` para los casos de prueba reproducibles.
