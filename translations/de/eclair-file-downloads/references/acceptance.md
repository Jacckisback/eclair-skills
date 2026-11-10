# Validierungsplan — Downloads

## Datenmodell
Datei, Titel, Version, Größe, tragende Seite.

## Erwartete Umsetzung
Die öffentlichen Dateien in der Mediathek ablegen, Dateigröße und Format anzeigen, ersetzte Dateien versionieren.

## Vorzusehende Tests
1. Normalfall: Jede Datei herunterladen und angegebenen Typ und angegebene Größe prüfen.
2. Ablehnungskontrolle: Eine ersetzte Datei lässt die alte Version nicht versehentlich zugänglich.
3. Invariante: Keine private oder kostenpflichtige Datei wird unter einer erratbaren öffentlichen Adresse abgelegt.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
