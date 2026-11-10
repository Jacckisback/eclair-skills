---
name: eclair-directory
description: "Indexierbare Einträge und Filter für ein Branchenverzeichnis erstellen. Use on Éclair CMS 2.x when the user wants to: indexierbare Einträge und Filter erstellen. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Branchenverzeichnis — Éclair CMS 2.x

## Auslöser und erwartetes Ergebnis
Diesen Skill verwenden, um Folgendes zu erreichen: **indexierbare Einträge und Filter erstellen**. Der **öffentliche Leseteil ist heute umsetzbar**; Schreibvorgänge durch Besucher erfordern mehr als der aktuelle Vertrag. Dieser Skill ist ein **Agenten-Workflow**, keine funktionsfähige PHP-Erweiterung und keine Konformitätsgarantie.

**WordPress-Entsprechung:** GeoDirectory, Business Directory Plugin. Familie: Business-Apps.

## Pflichtdiagnose vor jeder Änderung
1. `references/core-map.md` (was der Kern bereits leistet) und `references/native-contract.md` lesen; die tatsächliche Version des CMS und die Fähigkeiten in `GET /<admin>/api/capabilities` prüfen (sofern der Zugriff erlaubt ist).
2. `references/family-contract.md` und `references/acceptance.md` lesen. Niemals das alte Pack-System v0.x oder PHP-Code von WordPress in Éclair 2 kopieren.
3. Das Datenmodell ermitteln: **Eintrag, Kategorie, Standort, öffentlicher Kontakt, Verifizierungsstatus**. Dokumentieren, was öffentlich ist, was privat ist und woher jede Angabe stammt.

## Spezifisches Vorgehen
4. **Ablauf:** Öffentliche und private berufliche Daten trennen; Kategorieseiten, Canonical, Moderation und begrenzte Filter erstellen. Zustände und Fehler beschreiben, bevor Code geschrieben wird.
5. **Speicherorte:** websitespezifischer Code in `site/extensions/<id>/`, Erscheinungsbild in `site/themes/<id>/`, Daten unter `$ctx['data']`, Inhalte und Einstellungen über die Administration oder das MCP. Niemals `app/`, `assets/`, `index.php` oder den Updater bearbeiten.
6. **Aktueller Vertrag:** Öffentliche Schaufensterseiten sind mit GET möglich; Buchungen, Zahlungen, Bewerbungen, CRM und personenbezogene Daten erfordern gesichertes POST, geeigneten Speicher und serverseitig geprüfte Rechte.
7. **Sicherheitsinvariante:** Private Anschrift, Telefonnummer oder sensible Kontaktdaten nicht ohne Erlaubnis veröffentlichen. Außerdem die Rechte serverseitig, das Escaping mit `e()`, die Validierung der Daten sowie das Fehlen von Secrets oder personenbezogenen Daten im öffentlichen HTML oder in einem gemeinsamen Cache prüfen.
8. **Nachweise:** den Positivtest „Gefälschte Einträge, Dubletten, Löschung und leere Suche testen“ und den Ablehnungstest „Ein ausstehender Eintrag erscheint weder in der Sitemap noch in den strukturierten Daten“ schreiben. Regressionen bei SEO und Performance messen, den Rollback dokumentieren.
9. **Native Validierung:** `php tools/validate.php <dossier> --json`, `php tests/run.php` und `php tools/measure.php --check` auf einem offiziellen Checkout für jedes erzeugte Paket. Für einen vom Kern nicht unterstützten Teil einen Abweichungsvermerk und einen blockierenden Test liefern, niemals einen fiktiven Erfolg.

## Verpflichtende Liefergegenstände
- Mini-Spezifikation: Ziel, Benutzer, Abläufe, Zustände, Daten, Messungen.
- Berechtigungs- und Cache-Matrix: Route, Methode, Sitzung, Sichtbarkeit, Indexierung.
- Validiertes Nur-Lese-Paket (GET-Routen) und schriftlicher Plan für den Schreibteil, klar als nicht geliefert gekennzeichnet.
- Tests der Positivfälle und der Ablehnungen, Deaktivierungsverfahren, das die Daten erhält, Kompatibilitätsvermerk.

## Abnahmekriterien
- Gefälschte Einträge, Dubletten, Löschung und leere Suche testen.
- Ein ausstehender Eintrag erscheint weder in der Sitemap noch in den strukturierten Daten.
- Nichts wird ohne eine autorisierte Person veröffentlicht, aktiviert oder in Produktion gebracht; kein Score, kein Ranking und keine Zitierung durch eine KI wird versprochen.
- Die von Éclair 2.0 nicht unterstützten Teile sind ausdrücklich als **nicht produktionsreif lieferbar** gekennzeichnet.

**Reifegrad dieses Skills:** `public-read-only-prototype-possible`. Reproduzierbare Testfälle siehe `references/acceptance.md`.
