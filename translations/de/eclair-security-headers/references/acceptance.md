# Validierungsplan — Sicherheits-Header

## Datenmodell
HTTP-Header, Content-Security-Policy, HTTPS.

## Erwartete Umsetzung
Die ausgelieferten Header erfassen, HTTPS überall prüfen, die mit dem Kern gelieferten Webserver-Regeln testen.

## Vorzusehende Tests
1. Normalfall: Die Header einer öffentlichen Seite und der Administration analysieren.
2. Ablehnungskontrolle: Eine sensible Datei oder Datendatei wird niemals vom Webserver ausgeliefert.
3. Invariante: Kein Schutz-Header wird entfernt oder gelockert.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
