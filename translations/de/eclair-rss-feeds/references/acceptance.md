# Validierungsplan — RSS-Feeds

## Datenmodell
Feed, Einträge, Datum, vollständiger Inhalt oder Auszug.

## Erwartete Umsetzung
Den vom Kern erzeugten Feed kontrollieren, ihn in den Seiten deklarieren, ihn Abonnenten und Aggregatoren anbieten.

## Vorzusehende Tests
1. Normalfall: Den Feed mit einem Reader und einem Validator validieren.
2. Ablehnungskontrolle: Ein zurückgezogener Inhalt verschwindet bei der Neugenerierung aus dem Feed.
3. Invariante: Der Feed enthält nur veröffentlichte Inhalte.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
