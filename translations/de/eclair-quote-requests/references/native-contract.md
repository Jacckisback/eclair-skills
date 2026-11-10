# Anwendung des nativen Vertrags auf den Skill eclair-quote-requests

Dieser Skill verwendet ausschließlich das, was Éclair CMS 2.0.x ausliefert: die Funktionen des Kerns, den Theme-Vertrag und den Vertrag `eclair-extension/1`. Offizielle Referenz: https://github.com/Jacckisback/eclair-cms/blob/main/docs/EXTENSION-CONTRACT.md

## Position dieses Skills

Das öffentliche Lesen (GET, cachefähig) ist heute umsetzbar. Jeder Schreibvorgang durch einen Besucher erfordert eine öffentliche POST-Route, die der Kern 2.0 für Erweiterungen nicht öffnet (PR #19 im Entwurf, nicht gemergt): sie nicht simulieren.

## Praktische Leitplanke

Auf einem echten Checkout `eclair/index.php` erneut lesen, `php tools/validate.php` für jedes erzeugte Paket sowie `php tests/run.php` ausführen. Geht die Anfrage über die nativen Funktionen, die öffentlichen GET-Routen, die geschützten Administrationsseiten, die Blöcke, die Einstellungen und `Store` hinaus, eine gesonderte Anfrage zur Weiterentwicklung erstellen; **niemals deren Verfügbarkeit vortäuschen**.
