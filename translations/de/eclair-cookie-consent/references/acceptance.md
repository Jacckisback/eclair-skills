# Validierungsplan — Cookies und Einwilligung

## Datenmodell
Tracker, Zweck, Einwilligung, Nachweis.

## Erwartete Umsetzung
Die tatsächlichen Tracker inventarisieren; ohne Tracker kein Banner; andernfalls vorherige Einwilligung, Ablehnung so einfach wie Zustimmung und Informationsseite.

## Vorzusehende Tests
1. Normalfall: Cookies und Anfragen vor und nach der Auswahl untersuchen.
2. Ablehnungskontrolle: Nach einer Ablehnung wird kein Drittanbieter-Tracker geladen.
3. Invariante: Kein einwilligungspflichtiger Tracker wird vor der Zustimmung gesetzt.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
