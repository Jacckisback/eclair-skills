# Validierungsplan — Ankündigungsleisten

## Datenmodell
Nachricht, Link, Start- und Enddatum.

## Erwartete Umsetzung
Die Leiste serverseitig mit Gültigkeitsdaten ausgeben, ohne Layoutverschiebung, bei Fristablauf automatisch entfernt.

## Vorzusehende Tests
1. Normalfall: Eine Leiste anzeigen, schließen und ablaufen lassen.
2. Ablehnungskontrolle: Nach dem Enddatum erscheint die Leiste auf keiner Seite mehr.
3. Invariante: Keine abgelaufene Ankündigung wird weiterhin aus dem Cache ausgeliefert.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
