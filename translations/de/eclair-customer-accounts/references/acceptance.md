# Validierungsplan — Kundenkonten

## Datenmodell
Kunde, Zugangsdaten, Bestellungen, Adressen.

## Erwartete Umsetzung
Registrierung, Anmeldung, Wiederherstellung und Löschung des Kontos festlegen; Kundenkonten und Administrationskonten strikt trennen.

## Vorzusehende Tests
1. Normalfall: Registrierung, Anmeldung, Einsicht und Löschung des Kontos simulieren.
2. Ablehnungskontrolle: Ein Kunde kann die Bestellung eines anderen nicht lesen, indem er eine Kennung ändert.
3. Invariante: Ein Kunde sieht nur seine eigenen Daten; niemals ein gemeinsamer Cache im Kundenbereich.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
