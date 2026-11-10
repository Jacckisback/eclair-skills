# Validierungsplan — Verzögertes Laden

## Datenmodell
Bild, Priorität, Abmessungen.

## Erwartete Umsetzung
Prüfen, dass das Hauptbild mit Priorität und die anderen verzögert geladen werden, mit ausdrücklichen Abmessungen.

## Vorzusehende Tests
1. Normalfall: Die Anzeige des größten Elements und die Layoutverschiebung messen.
2. Ablehnungskontrolle: Das Hauptbild wird niemals verzögert geladen.
3. Invariante: Kein Drittanbieter-Skript wird hinzugefügt, um das Laden zu verzögern.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
