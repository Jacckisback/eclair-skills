# Vertrag der Familie Inhalte & Redaktion

Ziel: **Éclair CMS 2.0.x**, Erweiterung **`eclair-extension/1`**, Kennungen und Version vor jeder Änderung ermittelt.

**Bevorzugt zu nutzende native Fähigkeiten:** bereits in den Kern integrierte Funktionen (siehe `core-map.md`), Themes in `site/themes/`, Erweiterungen in `site/extensions/`, `Store`-Daten unter `$ctx['data']`, öffentliche GET-Routen und geschützte GET/POST-Routen der Administration, geplante Aufgaben, Migrationen, Validierung mit `tools/validate.php`, PHP-Suite, Messungen.

**Einschränkungen für die Produktion:** Inhalte und ihre Veröffentlichung laufen über die Administration oder den MCP-Connector, als Entwurf; benutzerdefinierte Inhaltstypen und Schreibvorgänge von Besuchern (Kommentare) sind in 2.0 für Erweiterungen nicht geöffnet.

**Agenten-Richtlinie:** zuerst das Native nutzen, das Minimum an Code erzeugen, den Kern unangetastet lassen, es ablehnen, ein Mockup als in Betrieb befindliche Funktionalität darzustellen; eine Weiterentwicklung des Kerns anfordern, wenn sie nötig ist. Änderungen mit großer Tragweite (Zahlung, private Inhalte, E-Mails, personenbezogene oder Gesundheitsdaten) erfordern reale Tests und eine menschliche Freigabe vor der Aktivierung.

**Sicherheitspunkte:** jedes Objekt und jeden Schreibvorgang kontrollieren; Formulare, Secrets, Signaturen und personenbezogene Daten schützen; Fehler und Rollback prüfen; im öffentlichen Cache nur HTML ohne Benutzerdaten halten. `eclair-extension/1` nicht mit den früheren experimentellen APIs verwechseln.
