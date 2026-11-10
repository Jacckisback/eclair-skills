# Validierungsplan — Aufgaben und Korrekturen

## Datenmodell
Aufgabe, Abgabe, Note, Kommentar, Lernender.

## Erwartete Umsetzung
Abgabe, Fristen, Korrektur und Rückmeldung festlegen; jede Arbeit auf ihren Autor und den Korrektor abschotten.

## Vorzusehende Tests
1. Normalfall: Abgabe, Korrektur und Einsicht in die Note simulieren.
2. Ablehnungskontrolle: Ein Lernender kann nicht auf die Arbeit eines anderen zugreifen.
3. Invariante: Eine Arbeit ist nur für ihren Autor und die benannten Korrektoren lesbar.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
