# Validierungsplan — Schutz der Anmeldung

## Datenmodell
Versuche, Limits je Netzwerk und je Konto, Administrationsadresse.

## Erwartete Umsetzung
Die nativen Versuchslimits, die Administrationsadresse, die aktiven Sitzungen und die vorläufigen Passwörter kontrollieren.

## Vorzusehende Tests
1. Normalfall: Wiederholte Fehlversuche simulieren und die Sperrung feststellen.
2. Ablehnungskontrolle: Das gewohnte Gerät des Eigentümers wird durch die Versuche eines Dritten nicht gesperrt.
3. Invariante: Kein natives Limit wird gelockert.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
