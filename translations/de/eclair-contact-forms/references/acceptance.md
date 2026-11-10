# Validierungsplan — Kontaktformular

## Datenmodell
Nachricht, Name, E-Mail, Betreff, Datum, Lesestatus.

## Erwartete Umsetzung
Den nativen Kontakt-Block platzieren, den Empfänger einstellen, Versand und Empfang testen, den Informationshinweis anzeigen.

## Vorzusehende Tests
1. Normalfall: Eine echte Nachricht senden und sie in der Administration und per E-Mail wiederfinden.
2. Ablehnungskontrolle: Wiederholte Sendungen in schneller Folge werden vom Kern begrenzt.
3. Invariante: Die Nachrichten sind nur für Konten mit dem Recht Nachrichten sichtbar.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
