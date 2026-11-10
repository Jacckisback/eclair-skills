# Validierungsplan — Formulare und Mini-CRM

## Datenmodell
Formular, Feld, Einwilligung, Kontakt, Quelle, Ticket und Status.

## Erwartete Umsetzung
Zweck und Aufbewahrungsdauer je Formular festlegen; Daten serverseitig validieren; vor Spam schützen; Dateien und Leserecht abschotten.

## Vorzusehende Tests
1. Normalfall: Spam, Anhang, Dublette und DSGVO-Löschung testen.
2. Ablehnungskontrolle: Ein Benutzer ohne Recht kann die Kontaktdatenbank nicht exportieren.
3. Invariante: Ein öffentliches Formular darf keine E-Mail-Injection zulassen und die Daten nicht im Cache erscheinen lassen.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
