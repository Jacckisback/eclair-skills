# Validierungsplan — Werbung

## Datenmodell
Werbeplatz, Einwilligung, Datei ads.txt.

## Erwartete Umsetzung
Die native Seite Werbung verwenden, die Werbeplätze begrenzen, Einwilligung, Kennzeichnung und Auswirkung auf die Geschwindigkeit prüfen.

## Vorzusehende Tests
1. Normalfall: Die Seite mit und ohne Werbung messen und die Einwilligung prüfen.
2. Ablehnungskontrolle: Die Seiten außerhalb der Artikel zeigen keine Werbung an.
3. Invariante: Keine Werbung wird vor der erforderlichen Einwilligung geladen.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
