# Validierungsplan — Observability und Alarme

## Datenmodell
Strukturierte Logs, Fehler, Korrelationen, Metriken, Traces, Aufbewahrung.

## Erwartete Umsetzung
Nützliche Alarme festlegen, Daten anonymisieren, Aufgaben und Cache überwachen, Vorfall der Website und des Moduls unterscheiden, Runbook bereitstellen.

## Vorzusehende Tests
1. Normalfall: Anstieg der 5xx-Fehler, Verzögerung der Aufgaben und volle Festplatte testen.
2. Ablehnungskontrolle: Ein deaktiviertes Modul sendet keine Daten mehr und führt keine Aufgaben mehr aus.
3. Invariante: Kein Passwort, Token, keine Zahlung und keine rohe PII in den Logs; keine versteckte Telemetrie.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
