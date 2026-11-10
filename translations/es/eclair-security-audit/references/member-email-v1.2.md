# Referencia técnica — Member Directory v0.3.0 (Éclair v2.0.0, contrato POST experimental)

## Recorridos disponibles (todos cache:false)

| Método | Ruta | Función |
|---|---|---|
| GET/POST | `/membres/connexion` | Formulario / inicio de sesión de una cuenta activa |
| GET | `/membres/espace` | Perfil privado propio del token de sesión |
| POST | `/membres/deconnexion` | Cierre de sesión con CSRF propio de la sesión |
| GET/POST | `/membres/inscription` | Email de invitación, solo si `registration_enabled=true` |
| GET/POST | `/membres/verification` | Elegir la contraseña con prueba de email única |
| GET/POST | `/membres/recuperation` | Solicitar un email de recuperación si `recovery_enabled=true` |
| GET/POST | `/membres/reinitialisation` | Sustituir la contraseña con prueba única |

## Mecanismos

- Sin cuenta CMS/`Auth::can` para los clientes. Los perfiles `member` no contienen nunca roles `admin` ni `editor`.
- `MemberAccounts::provision` exige una contraseña provisional aleatoria y crea una cuenta `pending`. El enlace del email pide a la persona que elija su propia contraseña. El token de verificación caduca a los 30 minutos y un comprobante solo se utiliza una vez.
- `MemberAccounts::issueReset` emite únicamente para un miembro `active`; después `confirmReset` efectúa la mutación bajo bloqueo e incrementa `epoch`. Todos los tokens de sesión anteriores quedan invalidados.
- Se utiliza `Mail::send` (servicio de Éclair), pero no es un acuse de entrega. No prometer al usuario ningún éxito de entrega.
- Para enviar un email, la URL canónica configurada debe ser HTTPS y estar verificada. El dominio de la petición HTTP queda excluido del enlace de recuperación.
- Las páginas GET no efectúan ningún tratamiento de negocio; el POST exige HTTPS y `Security::checkFormToken`, y el patch del núcleo comprueba también estas condiciones.
- Limitadores por red / email, mensajes genéricos sobre las solicitudes, pruebas validadas dos veces (preflight antes del hash, después bajo bloqueo de almacenamiento).
- Ningún recurso personal pasa a la caché estática pública. Los enlaces con token deben quedar excluidos de los registros y de toda página externa cargada desde los formularios de confirmación.

## Límites explícitos

- Una cuenta pendiente cuyo email ha sido aceptado por el transporte pero nunca recibido necesita un recorrido de nueva invitación/asistencia, no proporcionado aquí.
- Los mensajes genéricos no eliminan totalmente la posibilidad de inferir la existencia de una cuenta por el tiempo de ejecución.
- Los tokens de email en la URL pueden aparecer en el historial del navegador o en logs: auditoría de la infraestructura obligatoria.
- El prototipo `Store` está limitado a 1 000 miembros y no es una base relacional transaccional multiarchivo.
- El contrato `eclair-extension/1` oficial **no** autoriza POST público sin patch. Toda instalación en un sitio real queda a la espera de su validación.
