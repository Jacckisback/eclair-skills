# Validierungsplan — Drittanbieter-Skripte

## Datenmodell
Skript, Zweck, Gewicht, Domain, erforderliche Einwilligung.

## Erwartete Umsetzung
Jede Skriptanfrage inventarisieren, eine Alternative ohne Skript suchen, die Blockierung durch die native Inhaltsrichtlinie dokumentieren, wenn sie besteht.

## Vorzusehende Tests
1. Normalfall: Gewicht und Anfragen vor und nach jeder akzeptierten Ergänzung messen.
2. Ablehnungskontrolle: Ein Skript von einer nicht zugelassenen Domain wird nicht ausgeführt.
3. Invariante: Kein Skript wird unter Umgehung der Content-Security-Policy eingeschleust.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
