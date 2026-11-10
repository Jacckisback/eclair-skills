# Validierungsplan — Zahlungslinks

## Datenmodell
Produkt oder Variante, Zahlungslink, Dienstleister.

## Erwartete Umsetzung
Den Link beim Dienstleister erstellen, ihn in die Produktseite oder die Variante einfügen, im Testmodus testen, Beleg und Erstattung auf Seiten des Dienstleisters prüfen.

## Vorzusehende Tests
1. Normalfall: Im Testmodus kaufen und Betrag und Beleg prüfen.
2. Ablehnungskontrolle: Ein Link zu einer nicht anerkannten Domain wird abgelehnt.
3. Invariante: Keine Bankdaten auf der Website; ein Link führt nur zur Domain des Dienstleisters.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
