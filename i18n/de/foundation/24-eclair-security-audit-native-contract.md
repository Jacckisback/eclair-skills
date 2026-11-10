# Anwendung des nativen Vertrags auf den Skill eclair-security-audit

Dieser Skill verwendet ausschließlich den mit Éclair CMS 2.0.0 ausgelieferten Vertrag `eclair-extension/1` und nicht die APIs der alten Prototypen. Offizielle Referenz: https://github.com/Jacckisback/eclair-cms/blob/main/docs/EXTENSION-CONTRACT.md

## Praktische Leitplanke

Auf einem echten Checkout `eclair/index.php` erneut lesen, `php tools/validate.php` für jedes erzeugte Paket sowie `php tests/run.php` ausführen. Geht der angeforderte Vertrag über öffentliche GET-Routen, Admin-Berechtigungen, Felder/Blöcke und `Store` hinaus, ein eigenes RFC erstellen; **niemals dessen Verfügbarkeit vortäuschen**.
