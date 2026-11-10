# Validierungsplan — Geplante Aufgaben

## Datenmodell
Aufgabe, Häufigkeit, letzter Lauf, Ergebnis.

## Erwartete Umsetzung
Die Aufgabe im Manifest deklarieren (höchstens einmal pro Stunde), die geheime Adresse des Kerns vom Scheduler des Hosters aus aufrufen, protokollieren.

## Vorzusehende Tests
1. Normalfall: Die Aufgabe zweimal hintereinander ausführen und eine einzige Wirkung prüfen.
2. Ablehnungskontrolle: Ein Aufruf ohne das geheime Token löst nichts aus.
3. Invariante: Die geheime Adresse der Aufgaben wird niemals veröffentlicht; jede Aufgabe ist idempotent.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
