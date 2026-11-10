# Validierungsplan — Newsletter-Anmeldung

## Datenmodell
E-Mail-Adresse, Einwilligung, Datum, Quelle.

## Erwartete Umsetzung
Eine vom E-Mail-Marketing-Dienst gehostete Anmeldeseite oder einen Link verwenden, solange die Website selbst keine Anmeldung entgegennehmen kann; doppelte Bestätigung.

## Vorzusehende Tests
1. Normalfall: Sich anmelden, bestätigen, sich abmelden.
2. Ablehnungskontrolle: Eine nicht bestätigte Anmeldung erhält keinen Versand.
3. Invariante: Keine Adresse wird ohne ausdrückliche Einwilligung und Nachweis in eine Liste aufgenommen.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
