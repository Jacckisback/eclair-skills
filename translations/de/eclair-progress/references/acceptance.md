# Validierungsplan — Fortschrittsverfolgung

## Datenmodell
Einschreibung, Einheit, Abschlusszustand, Versuch, Dauer, Revision.

## Erwartete Umsetzung
Abschlussregeln festlegen; Fortschritt unter Zugriffskontrolle speichern; Einheiten versionieren; aus autorisierten Zuständen berechneten Fortschritt aggregieren.

## Vorzusehende Tests
1. Normalfall: Wiederaufnahme der Sitzung, zwei Geräte, entfernte Lektion testen.
2. Ablehnungskontrolle: Zwei Geräte dürfen den bereits bestätigten Fortschritt nicht zurückstufen.
3. Invariante: Fortschritte sind individuelle, nicht cachebare Daten; niemals eine beliebige Mitgliedskennung akzeptieren.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
