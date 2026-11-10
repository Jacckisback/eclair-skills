# Aplicación del contrato nativo al skill eclair-tag-manager

Este skill utiliza exclusivamente lo que entrega Éclair CMS 2.0.x: las funciones del núcleo, el contrato de tema y el contrato `eclair-extension/1`. Referencia oficial: https://github.com/Jacckisback/eclair-cms/blob/main/docs/EXTENSION-CONTRACT.md

## Posición de este skill

Una parte depende de un punto de enganche ausente del contrato 2.0 (tipos de contenido, contribución SEO o JSON-LD, política de contenido por extensión, filtro de renderizado). Entregar la parte nativa y documentar con precisión la brecha, sin rodeos para eludirla.

## Salvaguarda práctica

En un checkout real, releer `eclair/index.php`, ejecutar `php tools/validate.php` sobre todo paquete producido y `php tests/run.php`. Si la petición supera las funciones nativas, las rutas GET públicas, las páginas de administración protegidas, los bloques, los ajustes y `Store`, elaborar una solicitud de evolución independiente; **no simular nunca su disponibilidad**.
