# Validierungsplan — Website-Einstellungen

## Datenmodell
Name, Beschreibung, Logo, Kontaktdaten, Sprache, Theme, Art Direction.

## Erwartete Umsetzung
Die Fähigkeiten der Website auslesen, die Einstellungen über die Administration eintragen, vor dem Speichern in der Vorschau prüfen.

## Vorzusehende Tests
1. Normalfall: Eine neue Website einstellen und die öffentliche Darstellung prüfen.
2. Ablehnungskontrolle: Ein Konto ohne das Recht Einstellungen ändert keine Einstellung.
3. Invariante: Kein nativer Schutz wird deaktiviert, um Zeit zu sparen.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
