# Validierungsplan — E-Mail-Marketing-Dienste

## Datenmodell
Liste, gehostetes Formular, API-Schlüssel, Synchronisierung.

## Erwartete Umsetzung
Das gehostete Formular des Dienstes verwenden; jeden API-Schlüssel in den Secrets der Erweiterung ablegen; bei Bedarf per Aufgabe synchronisieren.

## Vorzusehende Tests
1. Normalfall: Eine Testadresse anmelden und sie im Dienst wiederfinden.
2. Ablehnungskontrolle: Ein widerrufener Schlüssel erzeugt einen protokollierten Fehler, kein Leck.
3. Invariante: Kein API-Schlüssel im Code, im Repository oder auf einer öffentlichen Seite.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
