# Validierungsplan — Kurseinschreibungen

## Datenmodell
Mitglied, Kurs, Einschreibung, Zustand, Herkunft, Datum und Widerruf.

## Erwartete Umsetzung
Idempotente Einschreibung anlegen; Rechte je Objekt behandeln; kostenlose/kostenpflichtige Einschreibung unterscheiden; nach Erstattung gemäß ausdrücklicher Regel widerrufen.

## Vorzusehende Tests
1. Normalfall: Doppelkauf, Erstattung, Sperrung des Kontos testen.
2. Ablehnungskontrolle: Ein ausgeschlossenes Mitglied kann nicht mehr auf die zuvor freigegebenen Lektionen zugreifen.
3. Invariante: Niemals eine automatische Einschreibung allein aufgrund einer Rückkehr-URL des Zahlungsdienstleisters.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
