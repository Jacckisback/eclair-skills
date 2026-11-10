# Validierungsplan — Eingegangene Nachrichten

## Datenmodell
Nachricht, Status, Antwort, Aufbewahrungsdauer.

## Erwartete Umsetzung
Festlegen, wer liest und antwortet, innerhalb welcher Frist, wie lange die Nachrichten aufbewahrt und wie sie gelöscht werden.

## Vorzusehende Tests
1. Normalfall: Eine Nachricht vom Eingang bis zur Archivierung bearbeiten.
2. Ablehnungskontrolle: Ein Konto ohne das Recht Nachrichten greift auf keine Nachricht zu.
3. Invariante: Begrenzte Aufbewahrungsdauer und eingeschränktes Zugriffsrecht.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
