# Validierungsplan — Redaktioneller Workflow

## Datenmodell
Entwurf, Autor, Korrekturleser, geplantes Datum, Status, Planungseintrag.

## Erwartete Umsetzung
Anhand der nativen Rechte festlegen, wer schreibt und wer veröffentlicht, den Redaktionsplan und die Entwürfe nutzen, vor jeder Veröffentlichung eine menschliche Durchsicht beibehalten.

## Vorzusehende Tests
1. Normalfall: Einen Inhalt von der Idee zum Entwurf und dann zur Veröffentlichung durch eine befugte Person führen.
2. Ablehnungskontrolle: Ein auf Inhalte beschränktes Konto kann weder die Einstellungen ändern noch anstelle einer anderen Rolle veröffentlichen.
3. Invariante: Ein Agent oder ein Redakteur ohne Veröffentlichungsrecht stellt nichts online.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
