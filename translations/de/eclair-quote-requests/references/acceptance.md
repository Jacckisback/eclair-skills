# Validierungsplan — Angebotsanfragen

## Datenmodell
Anfrage, Leistung, Budget, Frist, Kontaktdaten.

## Erwartete Umsetzung
Mit dem nativen Kontaktformular und geführten Fragen auf der Seite beginnen; das strukturierte Formular für später konzipieren.

## Vorzusehende Tests
1. Normalfall: Eine Musteranfrage senden und ihren vollständigen Eingang prüfen.
2. Ablehnungskontrolle: Eine Anfrage ohne gültige Kontaktdaten wird mit einer klaren Meldung abgelehnt.
3. Invariante: Nur die für das Angebot nötigen Daten werden abgefragt.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
