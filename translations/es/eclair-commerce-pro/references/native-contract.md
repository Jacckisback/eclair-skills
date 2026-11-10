# Aplicación del contrato nativo al skill eclair-commerce-pro

Este skill utiliza exclusivamente lo que entrega Éclair CMS 2.0.x: las funciones del núcleo, el contrato de tema y el contrato `eclair-extension/1`. Referencia oficial: https://github.com/Jacckisback/eclair-cms/blob/main/docs/EXTENSION-CONTRACT.md

## Posición de este skill

El núcleo ya proporciona una tienda ligera (fichas de producto, variantes, categorías, enlaces de pago de un proveedor, feed de comerciante): utilizarla primero, sin duplicarla. Más allá de eso, el carrito, los pedidos y los pagos necesitan POST públicos, un almacenamiento transaccional fiable, webhooks autenticados e idempotencia; Éclair 2.0 oficial no proporciona todo eso. La PR #19 sigue siendo un borrador: no utilizar nunca una ruta POST no fusionada como prueba de compatibilidad.

## Salvaguarda práctica

En un checkout real, releer `eclair/index.php`, ejecutar `php tools/validate.php` sobre todo paquete producido y `php tests/run.php`. Si la petición supera las funciones nativas, las rutas GET públicas, las páginas de administración protegidas, los bloques, los ajustes y `Store`, elaborar una solicitud de evolución independiente; **no simular nunca su disponibilidad**.
