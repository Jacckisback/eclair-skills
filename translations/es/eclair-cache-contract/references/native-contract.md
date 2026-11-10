# Aplicación del contrato nativo al skill eclair-cache-contract

Este skill utiliza exclusivamente el contrato `eclair-extension/1` entregado en Éclair CMS 2.0.0 y no las API de los antiguos prototipos. Referencia oficial: https://github.com/Jacckisback/eclair-cms/blob/main/docs/EXTENSION-CONTRACT.md

## Salvaguarda práctica

En un checkout real, releer `eclair/index.php`, ejecutar `php tools/validate.php` sobre todo paquete producido y `php tests/run.php`. Si el contrato solicitado supera las rutas GET públicas, los permisos admin, los campos/bloques y `Store`, elaborar una RFC independiente; **no simular nunca su disponibilidad**.
