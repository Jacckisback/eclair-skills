# Validierungsplan — Branchenverzeichnis

## Datenmodell
Eintrag, Kategorie, Standort, öffentlicher Kontakt, Verifizierungsstatus.

## Erwartete Umsetzung
Öffentliche und private berufliche Daten trennen; Kategorieseiten, Canonical, Moderation und begrenzte Filter erstellen.

## Vorzusehende Tests
1. Normalfall: Gefälschte Einträge, Dubletten, Löschung und leere Suche testen.
2. Ablehnungskontrolle: Ein ausstehender Eintrag erscheint weder in der Sitemap noch in den strukturierten Daten.
3. Invariante: Private Anschrift, Telefonnummer oder sensible Kontaktdaten nicht ohne Erlaubnis veröffentlichen.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
