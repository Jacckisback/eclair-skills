# Validierungsplan — Staging und Livegang

## Datenmodell
Testkopie, Unterschiede, Checkliste für den Livegang.

## Erwartete Umsetzung
Eine Sicherung auf einer geschützten, nicht indexierbaren Subdomain wiederherstellen, dort Theme und Funktionen validieren, dann in der Produktion nachvollziehen.

## Vorzusehende Tests
1. Normalfall: Einen Theme-Wechsel von der Kopie bis zur Produktion durchspielen.
2. Ablehnungskontrolle: Die Testkopie ist weder indexiert noch ohne Authentifizierung zugänglich.
3. Invariante: Die Testkopie ist passwortgeschützt und für Bots gesperrt.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
