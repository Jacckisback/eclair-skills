# Éclair Member Directory — v1.0 reference

Se proporciona un demostrador nativo de Éclair 2.0 en `examples/extensions/member-directory/`, en la raíz de la distribución fuente; no se incluye en la copia autónoma del skill.

- `schema`: `eclair-extension/1`; `requires.eclair`: `>=2.0.0`.
- Rutas `admin`: GET raíz, POST `/create`, POST `/disable`; permiso `users`.
- Ninguna ruta pública. Ningún login público y no se envía ningún email de validación.
- `Store`: claves `ext/member-directory/...`, escritura bajo bloqueo, límite de 1 000 miembros a título experimental.
- Sesión de miembro distinta de las sesiones de la administración, token opaco de 256 bits con hash en reposo, revocación por epoch.
- Activación tras prueba de email: no proporcionada por la superficie HTTP. Un rol de miembro no puede ser `admin` ni `editor`.
- Instalador: copiar la extensión a `site/extensions/member-directory`, pasar `tools/validate.php` del núcleo 2.0, importar y activar manualmente solo en laboratorio.
- Para cuentas activas destinadas al público: RFC para POST público seguro, validación de email, rate limiting, flujo de reset y tests nativos. Ninguna ruta GET debe crear/modificar una cuenta o una sesión.
