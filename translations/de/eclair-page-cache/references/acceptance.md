# Validierungsplan — Seiten-Cache

## Datenmodell
Seite im Cache, Invalidierung, verbotene Varianten.

## Erwartete Umsetzung
Die Antwort aus dem Cache messen, ermitteln, was das Caching einer Erweiterungsroute verhindert, die Invalidierung bei einer Änderung prüfen.

## Vorzusehende Tests
1. Normalfall: Die Antwortzeit vor und nach einer Änderung messen.
2. Ablehnungskontrolle: Eine als nicht cachebar deklarierte Erweiterungsroute wird niemals aus dem Cache ausgeliefert.
3. Invariante: Keine Seite mit Sitzungs- oder personenbezogenen Daten gelangt in den gemeinsamen Cache.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
