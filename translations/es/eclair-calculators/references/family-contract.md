# Contrato de la familia Formularios

Objetivo: **Éclair CMS 2.0.x**, extensión **`eclair-extension/1`**, identificadores y versión descubiertos antes de cualquier modificación.

**Capacidades nativas que deben priorizarse:** funciones ya integradas en el núcleo (ver `core-map.md`), temas en `site/themes/`, extensiones en `site/extensions/`, datos `Store` bajo `$ctx['data']`, rutas GET públicas y GET/POST de administración protegidas, tareas programadas, migraciones, validación `tools/validate.php`, suite PHP, mediciones.

**Limitaciones de producción:** Solo el formulario de contacto nativo recibe envíos de visitantes en la 2.0; cualquier otro formulario con envío al servidor exige una ruta POST pública no abierta a las extensiones.

**Política del agente:** utilizar primero lo nativo, generar el mínimo de código, mantener intacto el núcleo, negarse a presentar una maqueta como una funcionalidad en servicio; solicitar una evolución del núcleo cuando sea necesaria. Los cambios de gran alcance (pagos, contenido privado, correos electrónicos, datos personales o de salud) exigen tests reales y una validación humana antes de la activación.

**Puntos de seguridad:** controlar cada objeto y cada escritura; proteger formularios, secretos, firmas y datos personales; comprobar errores y reversión; conservar en la caché pública únicamente HTML sin datos de usuario. No confundir `eclair-extension/1` con las API experimentales anteriores.
