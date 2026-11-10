# Validierungsplan — Support und Tickets

## Datenmodell
Ticket, Anfragender, Status, Nachrichtenverlauf, Priorität.

## Erwartete Umsetzung
Mit Kontaktformular und Posteingang beginnen; Status, Fristen und Nachverfolgungsbereich für später konzipieren.

## Vorzusehende Tests
1. Normalfall: Eine Anfrage von der Eröffnung bis zum Abschluss durchspielen.
2. Ablehnungskontrolle: Ein Ticket kann nicht durch Erraten seiner Nummer gelesen werden.
3. Invariante: Ein Anfragender sieht nur seine eigenen Tickets.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
