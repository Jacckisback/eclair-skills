# Validierungsplan — Spamschutz

## Datenmodell
Nachricht, Formular-Token, Frequenzlimit.

## Erwartete Umsetzung
Auf das Token und die Limits des nativen Formulars stützen, bei Bedarf ein Honeypot-Feld ergänzen, den Posteingang überwachen.

## Vorzusehende Tests
1. Normalfall: Eine legitime Nachricht und dann eine automatisierte Salve senden.
2. Ablehnungskontrolle: Eine Einsendung ohne gültiges Token wird abgewiesen.
3. Invariante: Kein Drittanbieter-Dienst erhält die Nachrichten der Besucher ohne vorherige Information.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
