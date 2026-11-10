# Validierungsplan — Verkaufsmessung

## Datenmodell
Trichter, bestätigte Bestellungen, Erstattungen, Conversion-Rate, Nettoumsätze, Einwilligungen.

## Erwartete Umsetzung
Ereignisse und Kennzahlen festlegen, ohne sensible Daten wiederzuverwenden; Bestellsummen, Gutschriften und Zahlungen abgleichen; eine aggregierte Übersicht vorsehen.

## Vorzusehende Tests
1. Normalfall: Umsätze nach Erstattung und Zählunterbrechung testen.
2. Ablehnungskontrolle: Die Aggregation darf weder dieselbe Zahlung doppelt zählen noch eine identifizierbare Bestellung preisgeben.
3. Invariante: Personenbezogene Analysedaten erfordern eine Rechtsgrundlage und dürfen nicht über den Cache nach außen dringen.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
