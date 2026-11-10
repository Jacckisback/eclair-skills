# Validierungsplan — Titel und Meta-Beschreibungen

## Datenmodell
Titel, Meta-Beschreibung, angestrebter Suchbegriff, Ergebnisvorschau.

## Erwartete Umsetzung
Für jede Seite einen einzigartigen Titel und eine einzigartige Beschreibung verfassen, den Live-Score des Editors als Hilfe nutzen, ohne ihn als Ziel zu behandeln.

## Vorzusehende Tests
1. Normalfall: Einzigartigkeit und Länge auf allen Seiten kontrollieren.
2. Ablehnungskontrolle: Zwei veröffentlichte Seiten haben nicht denselben Titel.
3. Invariante: Kein Positionsversprechen; kein Keyword-Stuffing.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
