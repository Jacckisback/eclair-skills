# Validierungsplan — Zeitleisten

## Datenmodell
Schritt, Datum, Titel, Text.

## Erwartete Umsetzung
Die Zeitleiste als geordnete, per CSS gestaltete Liste ausgeben, auf dem Mobilgerät einspaltig lesbar.

## Vorzusehende Tests
1. Normalfall: Lesereihenfolge und mobile Darstellung prüfen.
2. Ablehnungskontrolle: Ein Schritt ohne Datum bleibt lesbar und geordnet.
3. Invariante: Die angezeigten Daten und Fakten werden vom Kunden geliefert.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
