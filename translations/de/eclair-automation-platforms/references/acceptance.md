# Validierungsplan — Automatisierungsplattformen

## Datenmodell
Szenario, Auslöser, übermittelte Daten.

## Erwartete Umsetzung
Lesend bereitstellen, was die Plattform abfragen kann (Feeds, öffentliches JSON); den Empfang von Ereignissen für später konzipieren.

## Vorzusehende Tests
1. Normalfall: Einen öffentlichen Feed von der Plattform lesen lassen und ein Szenario auslösen.
2. Ablehnungskontrolle: Ein nicht authentifizierter eingehender Aufruf ändert nichts an der Website.
3. Invariante: Keine personenbezogenen Daten werden in einem öffentlichen Endpunkt offengelegt, um eine Automatisierung zu erleichtern.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
