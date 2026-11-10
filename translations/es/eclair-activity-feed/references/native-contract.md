# Aplicación del contrato nativo al skill eclair-activity-feed

Este skill utiliza exclusivamente lo que entrega Éclair CMS 2.0.x: las funciones del núcleo, el contrato de tema y el contrato `eclair-extension/1`. Referencia oficial: https://github.com/Jacckisback/eclair-cms/blob/main/docs/EXTENSION-CONTRACT.md

## Posición de este skill

Esta función requiere escrituras de visitantes, cuentas públicas, transacciones o eventos firmados que `eclair-extension/1` no proporciona en la 2.0. Entregar el diseño, una maqueta GET segura y tests bloqueantes; no anunciar nunca una puesta en producción.

## Salvaguarda práctica

En un checkout real, releer `eclair/index.php`, ejecutar `php tools/validate.php` sobre todo paquete producido y `php tests/run.php`. Si la petición supera las funciones nativas, las rutas GET públicas, las páginas de administración protegidas, los bloques, los ajustes y `Store`, elaborar una solicitud de evolución independiente; **no simular nunca su disponibilidad**.
