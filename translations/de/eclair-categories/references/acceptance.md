# Validierungsplan — Kategorien

## Datenmodell
Kategorie, Adresse, Beschreibung, zugeordnete Inhalte.

## Erwartete Umsetzung
Wenige stabile Kategorien festlegen, ihre Beschreibung verfassen, jeden Inhalt einer Hauptkategorie zuordnen.

## Vorzusehende Tests
1. Normalfall: Die Kategorien anlegen, die Inhalte zuordnen und die Kategorieseiten samt Paginierung prüfen.
2. Ablehnungskontrolle: Eine Kategorie ohne veröffentlichten Inhalt wird in der Navigation nicht angeboten.
3. Invariante: Keine leeren oder doppelten Kategorien anlegen, die die Website verwässern.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
