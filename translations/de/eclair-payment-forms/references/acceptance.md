# Validierungsplan — Zahlungsformulare

## Datenmodell
Leistung, Betrag, Zahlungslink des Dienstleisters.

## Erwartete Umsetzung
Den Link beim Zahlungsdienstleister erstellen, ihn auf einer klaren Seite mit Bedingungen anzeigen, nichts auf der Website speichern.

## Vorzusehende Tests
1. Normalfall: Im Testmodus bezahlen und Beleg und Rückkehrseite prüfen.
2. Ablehnungskontrolle: Ein im Browser geänderter Betrag hat keinerlei Auswirkung auf den eingezogenen Betrag.
3. Invariante: Keine Bankdaten laufen über die Website oder werden dort gespeichert.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
