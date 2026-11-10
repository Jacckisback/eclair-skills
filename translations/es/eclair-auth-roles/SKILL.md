---
name: eclair-auth-roles
description: Use when reviewing Éclair v2 admin rights or designing member, student, customer and moderator authentication beyond the admin-only built-in roles.
---

# Éclair Auth & Roles — distinguir admin y miembros

## Realidad v2
`Eclair\Auth` y `Users` controlan **la administración** con sus permisos (`content`, `settings`, `security`, etc.). No son un directorio de clientes, alumnos o miembros, y no deben desviarse hacia roles `customer/student`.

## Procedimiento
1. Consultar `Users`, `Auth`, `Admin`, `Security`, `Session`, `RateLimit` y el permiso requerido por cada ruta admin `eclair-extension/1`.
2. Para una función de administración, declarar `routes.admin[]` con el `right` exacto y apoyarse en la verificación CSRF del núcleo. Comprobar el acceso según cada rol existente.
3. Para un espacio público de clientes/alumnos: elaborar una RFC de proveedor de identidad o un componente de servidor dedicado y auditado con un almacenamiento adecuado; **no** exponer las rutas sensibles mediante GET público.
4. Definir la sesión de miembro independiente, las cookies `Secure/HttpOnly/SameSite`, las autenticaciones progresivas, rate limiting, recuperación y verificación de email.
5. Permisos: identificar sistemáticamente al sujeto mediante una sesión de servidor verificada y después controlar el objeto y el alcance (IDOR/BOLA) en cada petición.
6. Probar la ausencia de privilegios heredados del admin, el cambio de rol, la revocación, el reset, las condiciones de carrera de sesiones, el acceso entre cuentas, CSRF y el rechazo por defecto.

## Demostrador nativo v1.0
La extensión `examples/extensions/member-directory/` proporciona un ejemplo **solo admin** para Éclair 2.0:
- `routes.admin`: GET + POST (`users`) con controles reforzados en los handlers; `routes.public`: array vacío.
- `MemberAccounts` y `MemberSessions` siguen siendo independientes de `Eclair\Users/Auth/Session`; cuenta `pending` obligatoria en el aprovisionamiento.
- Los datos residen exclusivamente bajo `data/ext/member-directory/` mediante `Store`. Nunca en `data/users.php`.
- `MemberPermissions::allows` recibe un token de sesión verificado, no una identidad proporcionada por el llamante.
- No está activado ni el registro público, ni el envío de emails, ni la recuperación de contraseña, ni la gestión real de las sesiones HTTP.
- La API POST pública requiere una RFC/nuevo contrato del núcleo y una validación de extremo a extremo antes del despliegue.
Leer `references/member-directory-v1.md` antes de construir un LMS, un foro o un comercio.

## Entregables
Matriz de permisos y recursos, modelo de amenazas, plan de identidad, juegos de tests e indicación «native / RFC requerida».

## Éclair 2.0 — prototipo v1.1 (experimental)
El prototipo v1.1 dispone de handlers públicos GET formulario + POST inicio/cierre de sesión + GET espacio privado. Solo son válidos tras la incorporación aprobada del contrato POST. Sesiones de miembros distintas de las de los admins, token opaco, CSRF double-submit y CSRF de sesión en el cierre de sesión; ningún rol admin/editor concedido.

## Éclair 2.0 — registro y recuperación (v1.2 experimental)

Leer `references/member-email-v1.2.md` antes de cualquier petición de creación de cuentas de clientes/alumnos o de recuperación de contraseña. El módulo `member-directory` v0.3 utiliza rutas públicas POST **fuera del contrato oficial**; no prometer nunca una instalación directa en un Éclair 2.0 sin modificar ni activar los flujos de email sin una URL HTTPS verificada y tests nativos. Preferir el sistema de extensiones v2 a cualquier modificación de la antigua arquitectura v0.x. Mantener separadas las cuentas públicas y las de administración, rechazar toda caché compartida para las páginas de miembros y tratar los emails como no entregados mientras no exista ninguna confirmación.
