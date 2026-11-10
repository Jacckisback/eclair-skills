# Validierungsplan — Lern-Dashboard

## Datenmodell
Einschreibungen, Fortschritt, aggregierte Ergebnisse, Kursereignisse.

## Erwartete Umsetzung
Für die Lehrenden nützliche Metriken festlegen, nach Kurs und Berechtigung filtern; Erhebung reduzieren; Aufbewahrung und Export vorsehen.

## Vorzusehende Tests
1. Normalfall: Sichtbarkeit für Lehrende bei Kurs A vs. B testen.
2. Ablehnungskontrolle: Eine Abfrage aggregierter Statistiken darf die Identität eines dritten Lernenden nicht offenlegen.
3. Invariante: Die Statistiken eines Lernenden sind nur für die berechtigten Parteien sichtbar.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
