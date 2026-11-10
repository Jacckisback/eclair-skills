# Validierungsplan — Übersetzte Adressen

## Datenmodell
Adresse pro Sprache, Weiterleitungen, canonical, hreflang.

## Erwartete Umsetzung
Eine Adresskonvention pro Sprache festlegen, die Slugs vor der Veröffentlichung übersetzen, vom Kern erzeugtes canonical und hreflang prüfen.

## Vorzusehende Tests
1. Normalfall: canonical und hreflang jeder Version prüfen.
2. Ablehnungskontrolle: Zwei Sprachen teilen sich niemals dieselbe Adresse.
3. Invariante: Keine veröffentlichte Adresse wird ohne Weiterleitung geändert.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
