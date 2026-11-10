# Validierungsplan — Lokale Entwicklung

## Datenmodell
PHP-Version, Webserver, Kopie der Website, Testdaten.

## Erwartete Umsetzung
Dieselbe PHP-Version und dieselben Serverregeln installieren, eine anonymisierte Sicherung wiederherstellen, die Tests ausführen.

## Vorzusehende Tests
1. Normalfall: Die lokale Website starten und die Testsuite erfolgreich durchlaufen lassen.
2. Ablehnungskontrolle: Eine lokale Kopie versendet keine echte E-Mail.
3. Invariante: Die echten Kundendaten werden nicht ohne Anonymisierung lokal kopiert.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
