# Validierungsplan — Immobilienanzeigen

## Datenmodell
Objekt, Transaktion, gerundete Geolokalisierung, Fläche, Medium, Preis, Verfügbarkeit.

## Erwartete Umsetzung
Anzeigen versionieren, begrenzte Filter bereitstellen, Status verkauft/vermietet, Bilder und Besichtigungsanfragen verwalten.

## Vorzusehende Tests
1. Normalfall: Zurückgezogene Anzeigen, private Medien und Filter testen.
2. Ablehnungskontrolle: Ein gelöschtes Objekt erscheint nach dem Leeren nicht mehr in den Ergebnissen und im Cache.
3. Invariante: Genaue Adressen oder Kontaktdaten der Eigentümer nicht ohne Zweck und Erlaubnis offenlegen.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
