# Validierungsplan — Bestände und Reservierungen

## Datenmodell
SKU, Lager, physischer Bestand, reserviert, verfügbar, unveränderliche Bewegungen.

## Erwartete Umsetzung
Die Zu- und Abgangsbewegungen konzipieren; die Reservierung sperren; Ablauf und Kompensation behandeln; alle manuellen Korrekturen nachverfolgen.

## Vorzusehende Tests
1. Normalfall: Gleichzeitige Käufe des letzten Exemplars und die Freigabe nach Ablauf testen.
2. Ablehnungskontrolle: Zwei Käufer können nicht denselben letzten Bestand reservieren.
3. Invariante: Das cachefähige Lesen der Verfügbarkeit ist informativ; jeder Verkauf liest den Bestand in einer Transaktion erneut.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
