# Validierungsplan — Veranstaltungen und Tickets

## Datenmodell
Veranstaltung, Termin, Platzkategorie, Reservierung, Ticket, Scan, Erstattung.

## Erwartete Umsetzung
Kontingente je Termin trennen; eindeutige Tickets nach bestätigter Zahlung ausstellen; atomare Einlasskontrolle und Übertragung verwalten.

## Vorzusehende Tests
1. Normalfall: Doppelten Scan, Stornierung und gleichzeitiges letztes Ticket testen.
2. Ablehnungskontrolle: Dasselbe Ticket an zwei Eingängen vorgezeigt => ein einziger Einlass akzeptiert.
3. Invariante: QR-Code enthält keine personenbezogenen Daten im Klartext und erlaubt nicht mehrere Eintritte.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
