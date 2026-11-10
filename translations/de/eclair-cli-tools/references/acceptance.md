# Validierungsplan — Kommandozeilenwerkzeuge

## Datenmodell
Befehl, Eingabe, Ausgabe, Rückgabecode.

## Erwartete Umsetzung
Auf einem Checkout des Kerns Validator, Testsuite und Budgetmessung ausführen; diese Befehle in die CI des Projekts integrieren.

## Vorzusehende Tests
1. Normalfall: Ein Paket validieren und den JSON-Bericht lesen.
2. Ablehnungskontrolle: Ein ungültiges Paket lässt den Befehl und die CI fehlschlagen.
3. Invariante: Kein Befehl wird ohne Sicherung auf der Produktion ausgeführt.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
