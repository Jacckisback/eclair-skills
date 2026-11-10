# Validierungsplan — Produktfeed

## Datenmodell
Produkt, Preis, Verfügbarkeit, Bild, Kennungen.

## Erwartete Umsetzung
Die Produktseiten vervollständigen, den vom Kern erzeugten Feed kontrollieren, ihn im Händler-Tool anmelden, die Ablehnungen korrigieren.

## Vorzusehende Tests
1. Normalfall: Den Feed validieren und drei Produkte mit ihrer Produktseite vergleichen.
2. Ablehnungskontrolle: Ein nicht verfügbares Produkt wird nicht als vorrätig angezeigt.
3. Invariante: Preis und Verfügbarkeit im Feed sind die der öffentlichen Produktseite.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
