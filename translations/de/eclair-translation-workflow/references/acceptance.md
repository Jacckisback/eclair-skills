# Validierungsplan — Übersetzungsworkflow

## Datenmodell
Quellinhalt, Zielversion, Übersetzer, Status, Aktualisierungsdatum.

## Erwartete Umsetzung
Eine Übersicht der zu übersetzenden Inhalte führen, die Übersetzungen als Entwurf erstellen, von einem Sprecher der Sprache gegenlesen lassen, veraltete Versionen kennzeichnen.

## Vorzusehende Tests
1. Normalfall: Eine Seite übersetzen, gegenlesen lassen, veröffentlichen, dann die Quelle ändern und die Kennzeichnung prüfen.
2. Ablehnungskontrolle: Eine nicht gegengelesene Übersetzung bleibt im Entwurf.
3. Invariante: Keine juristische oder medizinische Übersetzung wird ohne qualifizierte Freigabe veröffentlicht.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
