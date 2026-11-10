# Validierungsplan — Interne Verlinkung

## Datenmodell
Quellseite, Zielseite, Ankertext, verwaiste Seiten.

## Erwartete Umsetzung
Die Links kartieren, die verwaisten Seiten aufspüren, nützliche Links mit beschreibenden Ankertexten hinzufügen.

## Vorzusehende Tests
1. Normalfall: Prüfen, dass jede wichtige Seite mindestens einen internen Link erhält.
2. Ablehnungskontrolle: Kein interner Link zeigt auf eine Weiterleitung oder einen Fehler.
3. Invariante: Kein Link wird automatisch ohne Durchsicht des Kontexts hinzugefügt.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
