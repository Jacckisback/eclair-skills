# Validierungsplan — Community-Benachrichtigungen

## Datenmodell
Abonnement, Erwähnung, Benachrichtigung, Kanal, Einstellung, Status.

## Erwartete Umsetzung
Ereignisse nach validiertem Schreibvorgang auslösen, zum Zeitpunkt des Lesens und des Versands nach Rechten filtern, Abbestellung anwenden.

## Vorzusehende Tests
1. Normalfall: Wiederholte Benachrichtigungen, Abbestellung und Entzug der Berechtigung testen.
2. Ablehnungskontrolle: Nach dem Widerruf des Zugriffs enthält keine neue Benachrichtigung einen privaten Auszug.
3. Invariante: Niemals Inhalte privater Kategorien in E-Mail, Push oder Digest preisgeben.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
