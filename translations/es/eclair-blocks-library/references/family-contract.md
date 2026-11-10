# Contrato de la familia Diseño y UX

Objetivo: **Éclair CMS 2.0.x**, extensión **`eclair-extension/1`**, identificadores y versión descubiertos antes de cualquier modificación.

**Capacidades nativas que deben priorizarse:** funciones ya integradas en el núcleo (ver `core-map.md`), temas en `site/themes/`, extensiones en `site/extensions/`, datos `Store` bajo `$ctx['data']`, rutas GET públicas y GET/POST de administración protegidas, tareas programadas, migraciones, validación `tools/validate.php`, suite PHP, mediciones.

**Limitaciones de producción:** Éclair v2 expone temas bajo site/themes y bloques declarativos de extensión. No modificar ni app/, ni index.php, ni la CSP, ni la generación de la caché; validar los temas mediante tools/validate.php.

**Política del agente:** utilizar primero lo nativo, generar el mínimo de código, mantener intacto el núcleo, negarse a presentar una maqueta como una funcionalidad en servicio; solicitar una evolución del núcleo cuando sea necesaria. Los cambios de gran alcance (pagos, contenido privado, correos electrónicos, datos personales o de salud) exigen tests reales y una validación humana antes de la activación.

**Puntos de seguridad:** controlar cada objeto y cada escritura; proteger formularios, secretos, firmas y datos personales; comprobar errores y reversión; conservar en la caché pública únicamente HTML sin datos de usuario. No confundir `eclair-extension/1` con las API experimentales anteriores.
