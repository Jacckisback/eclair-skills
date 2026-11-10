# Validierungsplan — Tabs

## Datenmodell
Tab, Titel, Panel.

## Erwartete Umsetzung
Einen Tab-Block mit ARIA-Rollen, Navigation per Pfeiltasten und Rückfall auf gestapelte Abschnitte aufbauen.

## Vorzusehende Tests
1. Normalfall: Die Tabs per Tastatur und Screenreader durchgehen.
2. Ablehnungskontrolle: Ohne JavaScript sind alle Panels sichtbar.
3. Invariante: Der gesamte Inhalt bleibt im HTML und ist damit ohne JavaScript lesbar.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
