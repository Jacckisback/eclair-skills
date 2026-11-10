# Validierungsplan — Glossar

## Datenmodell
Begriff, Definition, verwandte Begriffe.

## Erwartete Umsetzung
Eine klare Definition je Begriff verfassen, alphabetisch ordnen, die Begriffe mit den Inhalten verknüpfen, die sie verwenden.

## Vorzusehende Tests
1. Normalfall: Nach Buchstaben navigieren und den Links zwischen den Begriffen folgen.
2. Ablehnungskontrolle: Ein Begriff ohne bestätigte Definition wird nicht veröffentlicht.
3. Invariante: Keine Definition wird aus einer geschützten Quelle kopiert.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
