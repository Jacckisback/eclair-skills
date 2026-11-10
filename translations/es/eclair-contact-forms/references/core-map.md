# Éclair CMS 2.0.x — mapa del núcleo verificado

Referencia: repositorio público `Jacckisback/eclair-cms`, rama `main` verificada el 9 de noviembre de 2026, commit de referencia `6567d7642ea2227a598c4988e970d43e2e5e0e4f`. **Un agente debe volver a comprobar siempre el checkout real y `GET /<admin>/api/capabilities`**: esta nota es una instantánea, no una garantía de compatibilidad futura.

## 1. Ya integrado en el núcleo: configurar, no reconstruir

Antes de escribir la más mínima extensión, comprobar si la necesidad está cubierta de forma nativa:

- **Contenidos**: páginas y artículos en bloques, categorías, menús, autores, borradores, planificación editorial; bloques `paragraph`, `heading`, `list`, `quote`, `image`, `video`, `table`, `code`, `button`, `callout`, `divider`, `hero`, `features`, `faq`, `team`, `contact`.
- **Medios**: imágenes redimensionadas, recodificadas y convertidas a WebP responsivo, dimensiones explícitas, carga diferida.
- **Formulario de contacto** y bandeja de entrada de los mensajes (permiso `messages`).
- **SEO y GEO**: títulos y descripciones con análisis en directo, JSON-LD (organización o negocio local, artículo, FAQ, migas de pan), sitemap con imágenes y `hreflang`, feed RSS, Open Graph con imagen para compartir, redirecciones 301 y gestor de redirecciones, IndexNow, `llms.txt`, versión Markdown de cada página, política para los robots de IA.
- **Velocidad**: caché estática de cada página pública, CSS integrado, un único script público, ninguna cookie pública.
- **Seguridad**: autenticación en dos pasos, límites de intentos, Content-Security-Policy estricta, contenidos saneados, control de integridad, registro, actualizaciones firmadas con reversión.
- **Copias de seguridad**: descarga y envío programado a un almacenamiento remoto, restauración.
- **Tienda ligera**: fichas de producto, variantes, categorías, enlaces de pago de un proveedor, feed de comerciante; **sin carrito, sin pedidos y sin cuenta de cliente**.
- **Funciones incluidas**: afiliación, publicidad, planificación, importación de WordPress, recuperación de un sitio antiguo, seguimiento de los robots de IA.
- **Asistente de IA y conector MCP**: solo borradores y propuestas, nunca publicación ni eliminación.
- **Apariencia**: temas y direcciones artísticas, vista previa antes de guardar.

## 2. Dónde puede escribir un skill

- Código del núcleo: `eclair/app/`, `eclair/assets/`, `eclair/index.php` — **no editar nunca** para entregar una funcionalidad de sitio.
- Extensiones del sitio: `site/extensions/<id>/` con `extension.json`, `extension.php`, `lib/`, `assets/`, `lang/`.
- Temas del sitio: `site/themes/<id>/` con `theme.json`.
- Datos de una extensión: `Eclair\Store`, prefijo `$ctx['data']` (`data/ext/<id>/`), secretos en `data/ext/<id>/secrets.php`.
- Contenidos y ajustes: únicamente mediante la administración o el conector MCP.

## 3. Contrato `eclair-extension/1`

- Rutas públicas de una extensión: **solo GET**, declaradas en el manifiesto, cacheables o no.
- Administración: GET/POST bajo `/<admin>/x/<id>/...`, permisos del núcleo (`content`, `media`, `menus`, `categories`, `messages`, `redirects`, `settings`, `users`, `security`) y protección CSRF.
- Bloques y ajustes declarativos validados por el núcleo; tareas programadas (como máximo una vez por hora); migraciones idempotentes; recursos publicados.
- El código de una extensión es **de confianza, sin sandbox**: la importación y la activación exigen una persona autorizada.
- Validación: `php tools/validate.php <dossier> --json`, después `php tests/run.php` y `php tools/measure.php --check` en un checkout del núcleo.

## 4. Límites conocidos de la 2.0

- No hay ruta POST pública para las extensiones (PR #19 en borrador, no fusionada), por lo que no hay registro, comentario, pedido ni envío por parte de un visitante fuera del formulario de contacto nativo.
- No hay identidad pública (cliente, alumno, miembro) en el contrato nativo.
- No hay tipo de contenido propio de una extensión; no hay contribución SEO o JSON-LD por extensión; no hay política de contenido (CSP) por extensión; no hay filtro general de renderizado.
- Las etiquetas, los comentarios y los tipos de contenido personalizados de WordPress no se recuperan en la importación.
- Los antiguos prototipos Éclair Devkit v0.x estaban dirigidos al núcleo 1.14 y **no se aplican** a la 2.0.

Fuentes oficiales:
- https://github.com/Jacckisback/eclair-cms/blob/main/docs/EXTENSION-CONTRACT.md
- https://github.com/Jacckisback/eclair-cms/blob/main/docs/THEME-CONTRACT.md
- https://github.com/Jacckisback/eclair-cms/blob/main/docs/SKILLS-GUIDE.md
- https://github.com/Jacckisback/eclair-cms/blob/main/docs/ARCHITECTURE-2.md
- https://github.com/Jacckisback/eclair-cms/blob/main/docs/schemas/extension.schema.json
