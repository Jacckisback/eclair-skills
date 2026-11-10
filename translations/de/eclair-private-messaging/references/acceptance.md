# Validierungsplan — Private Nachrichten

## Datenmodell
Unterhaltung, Teilnehmer, Nachricht, Meldung.

## Erwartete Umsetzung
Blockierung, Meldung, Versandgrenzen und Aufbewahrung festlegen; keine Unterhaltung in einer Seite im Cache.

## Vorzusehende Tests
1. Normalfall: Austausch, Blockierung und Meldung simulieren.
2. Ablehnungskontrolle: Ein blockiertes Mitglied kann demjenigen, der es blockiert hat, nicht mehr schreiben.
3. Invariante: Eine Nachricht ist nur für ihre Teilnehmer lesbar.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
