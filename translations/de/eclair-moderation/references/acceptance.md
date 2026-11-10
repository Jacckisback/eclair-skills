# Validierungsplan — Moderation und Meldungen

## Datenmodell
Meldung, Grund, betroffenes Element, Entscheidung, Moderator, Audit.

## Erwartete Umsetzung
Bearbeitungswarteschlange, missbräuchliche Meldungen, Schwellen/Kontingente, Rollback und Gründe vorsehen; Entscheidungen protokollieren und Befugnisse je Rolle beschränken.

## Vorzusehende Tests
1. Normalfall: Moderator ohne globales Recht, gesperrten Benutzer und Einspruch testen.
2. Ablehnungskontrolle: Ein Moderator einer Kategorie kann die privaten Meldungen einer anderen nicht sehen.
3. Invariante: Keine automatische endgültige Löschung durch eine Meldung ohne Prüfung und Belege.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
