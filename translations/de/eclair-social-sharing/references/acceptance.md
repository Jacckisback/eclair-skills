# Validierungsplan — Teilen-Schaltflächen

## Datenmodell
Netzwerk, Adresse zum Teilen, Beschriftung.

## Erwartete Umsetzung
Einfache Links zum Teilen und die Share-API des Browsers als Progressive Enhancement verwenden.

## Vorzusehende Tests
1. Normalfall: Eine Seite vom Mobilgerät und vom Computer aus teilen.
2. Ablehnungskontrolle: Keine Drittanbieter-Anfrage vor dem Klick.
3. Invariante: Keine Schaltfläche lädt ein Skript oder einen Tracker eines Drittanbieters.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
