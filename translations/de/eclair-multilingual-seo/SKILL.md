---
name: eclair-multilingual-seo
description: "Mehrere Sprachen ohne Duplikate oder falsche Canonicals betreiben (hreflang). Use on Éclair CMS 2.x when the user wants to: mehrere Sprachen ohne Duplikate und ohne falsche canonical verwalten. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Mehrsprachiges SEO — Éclair CMS 2.x

## Auslöser und erwartetes Ergebnis
Diesen Skill verwenden, um Folgendes zu erreichen: **mehrere Sprachen ohne Duplikate und ohne falsche canonical verwalten**. Diese Funktion ist **heute umsetzbar** mit dem nativen Vertrag (Theme, Blöcke, GET-Routen, Administrationsseiten, Aufgaben). Dieser Skill ist ein **Agenten-Workflow**, keine funktionsfähige PHP-Erweiterung und keine Konformitätsgarantie.

**WordPress-Entsprechung:** WPML SEO, Polylang. Familie: SEO, GEO & Migration.

## Pflichtdiagnose vor jeder Änderung
1. `references/core-map.md` (was der Kern bereits leistet) und `references/native-contract.md` lesen; die tatsächliche Version des CMS und die Fähigkeiten in `GET /<admin>/api/capabilities` prüfen (sofern der Zugriff erlaubt ist).
2. `references/family-contract.md` und `references/acceptance.md` lesen. Niemals das alte Pack-System v0.x oder PHP-Code von WordPress in Éclair 2 kopieren.
3. Das Datenmodell ermitteln: **Sprache, URL der Übersetzung, wechselseitiges hreflang, Titel und Sitemap**. Dokumentieren, was öffentlich ist, was privat ist und woher jede Angabe stammt.

## Spezifisches Vorgehen
4. **Ablauf:** Veröffentlichte Sprachen inventarisieren, das Mapping der Übersetzungen festlegen, canonical pro Sprache, hreflang/x-default und das Fehlen aufdringlicher Weiterleitungen testen. Zustände und Fehler beschreiben, bevor Code geschrieben wird.
5. **Speicherorte:** websitespezifischer Code in `site/extensions/<id>/`, Erscheinungsbild in `site/themes/<id>/`, Daten unter `$ctx['data']`, Inhalte und Einstellungen über die Administration oder das MCP. Niemals `app/`, `assets/`, `index.php` oder den Updater bearbeiten.
6. **Aktueller Vertrag:** Grundlegendes SEO/GEO ist nativ. Erweiterungen verfügen noch nicht über eine universelle API zum Einfügen von JSON-LD; die Vertragslücke dokumentieren, statt am HTML oder mit Skripten zu basteln.
7. **Sicherheitsinvariante:** Keine ungeprüfte maschinelle Übersetzung als endgültige Seite verwenden. Außerdem die Rechte serverseitig, das Escaping mit `e()`, die Validierung der Daten sowie das Fehlen von Secrets oder personenbezogenen Daten im öffentlichen HTML oder in einem gemeinsamen Cache prüfen.
8. **Nachweise:** den Positivtest „Paare FR/ES/EN, fehlende Seiten und Sprachwechsel testen“ und den Ablehnungstest „Jeder hreflang-Link zeigt auf eine indexierbare und wechselseitig verknüpfte URL mit 200“ schreiben. Regressionen bei SEO und Performance messen, den Rollback dokumentieren.
9. **Native Validierung:** `php tools/validate.php <dossier> --json`, `php tests/run.php` und `php tools/measure.php --check` auf einem offiziellen Checkout für jedes erzeugte Paket. Für einen vom Kern nicht unterstützten Teil einen Abweichungsvermerk und einen blockierenden Test liefern, niemals einen fiktiven Erfolg.

## Verpflichtende Liefergegenstände
- Mini-Spezifikation: Ziel, Benutzer, Abläufe, Zustände, Daten, Messungen.
- Berechtigungs- und Cache-Matrix: Route, Methode, Sitzung, Sichtbarkeit, Indexierung.
- Validiertes Paket `extension.json`/`extension.php` oder validiertes Theme-Paket, nur wenn ein nativer Block oder eine native Einstellung nicht genügt.
- Tests der Positivfälle und der Ablehnungen, Deaktivierungsverfahren, das die Daten erhält, Kompatibilitätsvermerk.

## Abnahmekriterien
- Paare FR/ES/EN, fehlende Seiten und Sprachwechsel testen.
- Jeder hreflang-Link zeigt auf eine indexierbare und wechselseitig verknüpfte URL mit 200.
- Nichts wird ohne eine autorisierte Person veröffentlicht, aktiviert oder in Produktion gebracht; kein Score, kein Ranking und keine Zitierung durch eine KI wird versprochen.
- Die von Éclair 2.0 nicht unterstützten Teile sind ausdrücklich als **nicht produktionsreif lieferbar** gekennzeichnet.

**Reifegrad dieses Skills:** `native-v2-workflow`. Reproduzierbare Testfälle siehe `references/acceptance.md`.
