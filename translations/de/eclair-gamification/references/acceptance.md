# Validierungsplan — Abzeichen und Punkte

## Datenmodell
Regel, Punkte, Abzeichen, Rangliste.

## Erwartete Umsetzung
Einfache, serverseitig überprüfbare Regeln festlegen, Entzug bei Missbrauch und die Option vorsehen, nicht in der Rangliste zu erscheinen.

## Vorzusehende Tests
1. Normalfall: Gewinn, Entzug und Anzeige der Rangliste simulieren.
2. Ablehnungskontrolle: Eine künstlich wiederholte Aktion bringt keine doppelten Punkte ein.
3. Invariante: Kein Punkt wird im Vertrauen auf eine vom Browser gesendete Information vergeben.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
