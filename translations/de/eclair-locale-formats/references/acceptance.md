# Validierungsplan — Regionale Formate

## Datenmodell
Sprache, Land, Währung, Zeitzone.

## Erwartete Umsetzung
Die Formatierung serverseitig zentralisieren, niemals ein Format fest in die Vorlagen schreiben.

## Vorzusehende Tests
1. Normalfall: Ein Datum und einen Preis auf Französisch, Englisch und Deutsch vergleichen.
2. Ablehnungskontrolle: Eine unbekannte Währung wird nicht mit einem irreführenden Standardsymbol angezeigt.
3. Invariante: Ein angezeigter Preis entspricht immer der tatsächlich berechneten Währung.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
