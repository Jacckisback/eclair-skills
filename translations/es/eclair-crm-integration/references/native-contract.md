# Aplicación del contrato nativo al skill eclair-crm-integration

Este skill utiliza exclusivamente lo que entrega Éclair CMS 2.0.x: las funciones del núcleo, el contrato de tema y el contrato `eclair-extension/1`. Referencia oficial: https://github.com/Jacckisback/eclair-cms/blob/main/docs/EXTENSION-CONTRACT.md

## Posición de este skill

Las tareas nativas existen (mínimo 3 600 segundos). Los webhooks entrantes y las interacciones de miembros requieren rutas POST cualificadas, una validación de firma y, para los efectos de negocio, una outbox idempotente.

## Salvaguarda práctica

En un checkout real, releer `eclair/index.php`, ejecutar `php tools/validate.php` sobre todo paquete producido y `php tests/run.php`. Si la petición supera las funciones nativas, las rutas GET públicas, las páginas de administración protegidas, los bloques, los ajustes y `Store`, elaborar una solicitud de evolución independiente; **no simular nunca su disponibilidad**.
