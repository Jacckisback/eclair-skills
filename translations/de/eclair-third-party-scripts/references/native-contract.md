# Anwendung des nativen Vertrags auf den Skill eclair-third-party-scripts

Dieser Skill verwendet ausschließlich das, was Éclair CMS 2.0.x ausliefert: die Funktionen des Kerns, den Theme-Vertrag und den Vertrag `eclair-extension/1`. Offizielle Referenz: https://github.com/Jacckisback/eclair-cms/blob/main/docs/EXTENSION-CONTRACT.md

## Position dieses Skills

Ein Teil hängt von einem Hook ab, der im Vertrag 2.0 fehlt (Inhaltstypen, SEO- oder JSON-LD-Beitrag, Inhaltsrichtlinie pro Erweiterung, Rendering-Filter). Den nativen Teil liefern und die Lücke präzise dokumentieren, ohne Workaround.

## Praktische Leitplanke

Auf einem echten Checkout `eclair/index.php` erneut lesen, `php tools/validate.php` für jedes erzeugte Paket sowie `php tests/run.php` ausführen. Geht die Anfrage über die nativen Funktionen, die öffentlichen GET-Routen, die geschützten Administrationsseiten, die Blöcke, die Einstellungen und `Store` hinaus, eine gesonderte Anfrage zur Weiterentwicklung erstellen; **niemals deren Verfügbarkeit vortäuschen**.
