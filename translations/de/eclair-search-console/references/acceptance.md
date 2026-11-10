# Validierungsplan — Search Console

## Datenmodell
Property, Verifizierungsmethode, eingereichte Sitemap, Berichte.

## Erwartete Umsetzung
Die Domain per DNS-Eintrag verifizieren, die native Sitemap einreichen, Abdeckung und Suchanfragen jeden Monat auswerten.

## Vorzusehende Tests
1. Normalfall: Die Property verifizieren und prüfen, dass die Sitemap berücksichtigt wird.
2. Ablehnungskontrolle: Ein Abdeckungsfehler wird erklärt, nicht verborgen.
3. Invariante: Kein Inhaberzugriff wird ohne Zustimmung des Kunden an Dritte vergeben.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
