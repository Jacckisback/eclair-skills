# Validierungsplan — Abonnements und Mitgliedschaften

## Datenmodell
Tarif, Mitgliedschaft, Verlängerung, Zeitraum, Kündigung, Zahlung, Recht.

## Erwartete Umsetzung
Rechte aus dem verifizierten Zustand berechnen, Tarifwechsel und Kulanzfristen vorsehen, Abrechnungsereignisse idempotent behandeln.

## Vorzusehende Tests
1. Normalfall: Fehlgeschlagene Abbuchung, anteilige Berechnung, Erstattung und Kündigung testen.
2. Ablehnungskontrolle: Zwei identische Ereignisse verlängern das Abonnement nicht zweimal.
3. Invariante: Ein Beleg aus dem Browser genügt niemals, um einen kostenpflichtigen Zugriff zu verlängern.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
