# Validierungsplan — Paginierung und Listen

## Datenmodell
Liste, aktuelle Seite, Seitengröße, Links zurück und weiter.

## Erwartete Umsetzung
Eine vernünftige Seitengröße, stabile Adressen pro Seite und barrierefreie Links festlegen.

## Vorzusehende Tests
1. Normalfall: Die erste, eine mittlere und die letzte Seite durchgehen.
2. Ablehnungskontrolle: Eine Seitennummer außerhalb der Grenzen antwortet mit einem sauberen Fehler, nicht mit einer leeren, indexierbaren Liste.
3. Invariante: Die Seitenparameter sind begrenzt und validiert.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
