---
name: eclair-security-audit
description: Use when auditing Éclair CMS 2.0 native extensions, package supply chain, admin actions, member data and future commerce/LMS security.
---

# Éclair Security Audit — revisión antes de la activación

## Alcance
1. Establecer la versión del núcleo, la procedencia de la extensión, los archivos ejecutables y los permisos reclamados.
2. Exigir un contrato `extension.json` conforme y huellas SHA-256 para los archivos; comprobar symlinks, rutas con salto de directorio, scripts imprevistos, ZIP bombs, tamaños, métodos y rutas reservadas.
3. Controlar por separado el `right` nativo de la ruta admin y las autorizaciones de negocio sobre los objetos; un permiso `content` no autoriza a leer el pedido de otro cliente.
4. Probar CSRF, rate limiting, session fixation, acceso directo a los archivos, XSS en el HTML devuelto, inyección SQL, SSRF de las URL externas y gestión de los secretos.
5. Páginas públicas con `cache:true`: ausencia de datos personales y de variantes por usuario. Páginas admin: headers, autenticación y rechazo por defecto.
6. Para un checkout: webhook firmado con verificación en el servidor, idempotencia, importes, divisa, IVA y transiciones de estado transaccionales antes de la entrega.
7. Para eventos de negocio: recordar que v2 no integra ningún bus/outbox estándar; proyecto aparte con tests de fallo y ninguna promesa de exactly-once para efectos remotos.
8. No ejecutar nunca módulos no auditados con la confianza del proceso PHP.

## Pruebas mínimas
`php tools/validate.php chemin/extension --json`, `php tests/run.php`, `php tools/measure.php --check` y escenarios negativos HTTP sobre una instalación de prueba. Ningún informe de seguridad es una certificación automática.

## Entregables
Lista de riesgos clasificados, demostraciones reproducibles, correcciones, límites restantes y decisión explícita Go/No-Go.

## V1.0 — Tests de la identidad
Auditar el prototipo `member-directory`: ninguna cuenta de miembro en `data/users.php`, contraseña nunca devuelta, estado `pending` por defecto, roles `admin/editor` prohibidos, epoch de revocación, control de objeto propio/ajeno, cookie `__Host-` HTTPS. Los tests locales no equivalen a una auditoría en producción.

## Éclair 2.0 — prototipo v1.1 (experimental)
El prototipo v1.1 tiene una limitación `RateLimit::attempt` antes del hash, una separación estricta miembros/admin y tokens de sesión de 256 bits. Evaluar la seguridad de los `Origin`, de TLS detrás de un reverse proxy, CSRF, IDOR, enumeración de cuentas, fugas de información y concurrencia. No confundir tests aislados con una auditoría en producción.

## Éclair 2.0 — registro y recuperación (v1.2 experimental)

Leer `references/member-email-v1.2.md` antes de cualquier petición de creación de cuentas de clientes/alumnos o de recuperación de contraseña. El módulo `member-directory` v0.3 utiliza rutas públicas POST **fuera del contrato oficial**; no prometer nunca una instalación directa en un Éclair 2.0 sin modificar ni activar los flujos de email sin una URL HTTPS verificada y tests nativos. Preferir el sistema de extensiones v2 a cualquier modificación de la antigua arquitectura v0.x. Mantener separadas las cuentas públicas y las de administración, rechazar toda caché compartida para las páginas de miembros y tratar los emails como no entregados mientras no exista ninguna confirmación.
