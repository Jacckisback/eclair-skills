# Validierungsplan — Forensuche

## Datenmodell
Begriff, begrenzter Index, Sprache, Kategorie, Seite, Status und Rechte.

## Erwartete Umsetzung
Text normalisieren, die freigegebenen Veröffentlichungen indexieren, paginieren und Kosten begrenzen, gelöschte Objekte aus dem Ergebnis entfernen.

## Vorzusehende Tests
1. Normalfall: Leere Eingabe, Injection, massenhafte Suche, private Themen testen.
2. Ablehnungskontrolle: Ein Besucher darf den Auszug einer privaten Diskussion nicht in einem Vorschlag sehen.
3. Invariante: Die Filterung nach Berechtigungen erfolgt bei jeder Suche, nicht nur zum Zeitpunkt der Indexierung.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
