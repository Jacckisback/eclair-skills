# Validierungsplan — Rezepte

## Datenmodell
Rezept, Zutaten, Schritte, Zeit, Portionen.

## Erwartete Umsetzung
Jedes Rezept in Zutaten und Schritte gliedern, Zeit und Portionen ergänzen, eine druckbare Version vorsehen.

## Vorzusehende Tests
1. Normalfall: Einem veröffentlichten Rezept auf dem Mobilgerät folgen und es ausdrucken.
2. Ablehnungskontrolle: Ein Rezept ohne Mengenangaben wird nicht veröffentlicht.
3. Invariante: Keine unbelegte gesundheitsbezogene Angabe.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
