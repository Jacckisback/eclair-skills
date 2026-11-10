# Validierungsplan — Diagnose und Protokolle

## Datenmodell
Symptom, Serverprotokoll, Website-Protokoll, Hypothese, Korrektur.

## Erwartete Umsetzung
Reproduzieren, die Protokolle des Servers und der Website lesen, die verursachende Funktion durch Deaktivieren isolieren, korrigieren und dann prüfen.

## Vorzusehende Tests
1. Normalfall: In einer Testerweiterung einen Fehler auslösen und ihn lokalisieren.
2. Ablehnungskontrolle: Auf einer öffentlichen Seite erscheint kein technischer Trace.
3. Invariante: Die Fehleranzeige wird auf der öffentlichen Website niemals aktiviert.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
