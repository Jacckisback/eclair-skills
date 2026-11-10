# Validierungsplan — Mehrsprachige Inhalte

## Datenmodell
Inhalt, Sprache, verknüpfte Version, Adresse pro Sprache.

## Erwartete Umsetzung
In den Fähigkeiten die von der Website unterstützten Sprachen prüfen, eine Seitenstruktur pro Sprache aufbauen, die Versionen verknüpfen und hreflang kontrollieren.

## Vorzusehende Tests
1. Normalfall: Eine Seite in zwei Sprachen anlegen und Querverweise und hreflang prüfen.
2. Ablehnungskontrolle: Eine Sprache ohne Übersetzung verweist nicht auf eine leere Seite.
3. Invariante: Keine maschinelle Übersetzung wird ohne menschliche Durchsicht veröffentlicht.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
