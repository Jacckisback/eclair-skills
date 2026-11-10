---
name: eclair-product-variants
description: "Größen, Farben und Konfigurationen ohne Preisfehler modellieren. Use on Éclair CMS 2.x when the user wants to: Größen, Farben und Konfigurationen ohne Preisfehler modellieren. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Varianten und Attribute — Éclair CMS 2.x

## Auslöser und erwartetes Ergebnis
Diesen Skill verwenden, um Folgendes zu erreichen: **Größen, Farben und Konfigurationen ohne Preisfehler modellieren**. Diese Funktion ist **bereits in den Kern von Éclair 2.0 integriert**: Der Skill leitet ihre Konfiguration und Überprüfung an, ohne eine Erweiterung zu schreiben. Dieser Skill ist ein **Agenten-Workflow**, keine funktionsfähige PHP-Erweiterung und keine Konformitätsgarantie.

**WordPress-Entsprechung:** Variable Produkte von WooCommerce. Familie: Commerce Pro.

## Pflichtdiagnose vor jeder Änderung
1. `references/core-map.md` (was der Kern bereits leistet) und `references/native-contract.md` lesen; die tatsächliche Version des CMS und die Fähigkeiten in `GET /<admin>/api/capabilities` prüfen (sofern der Zugriff erlaubt ist).
2. `references/family-contract.md` und `references/acceptance.md` lesen. Niemals das alte Pack-System v0.x oder PHP-Code von WordPress in Éclair 2 kopieren.
3. Das Datenmodell ermitteln: **Übergeordnetes Produkt, Varianten mit eindeutiger SKU, Attributkombinationen, eigene Preise/Bestände, Medium und Status**. Dokumentieren, was öffentlich ist, was privat ist und woher jede Angabe stammt.

## Spezifisches Vorgehen
4. **Ablauf:** Die maximale Anzahl der Kombinationen festlegen; die Eindeutigkeit der SKU sicherstellen; die Varianten in die GET-Ausgabe projizieren; eine beim Checkout serverseitig validierte Auswahl vorbereiten. Zustände und Fehler beschreiben, bevor Code geschrieben wird.
5. **Speicherorte:** websitespezifischer Code in `site/extensions/<id>/`, Erscheinungsbild in `site/themes/<id>/`, Daten unter `$ctx['data']`, Inhalte und Einstellungen über die Administration oder das MCP. Niemals `app/`, `assets/`, `index.php` oder den Updater bearbeiten.
6. **Aktueller Vertrag:** Der Kern liefert bereits einen leichtgewichtigen Shop (Produktseiten, Varianten, Kategorien, Zahlungslinks eines Anbieters, Händler-Feed): ihn zuerst nutzen, ohne ihn zu duplizieren. Darüber hinaus gilt: Warenkorb, Bestellungen und Zahlungen benötigen öffentliche POSTs, einen zuverlässigen transaktionalen Speicher, authentifizierte Webhooks und Idempotenz; das offizielle Éclair 2.0 stellt all das nicht bereit. Die PR #19 ist noch ein Entwurf: niemals eine nicht gemergte POST-Route als Kompatibilitätsnachweis verwenden.
7. **Sicherheitsinvariante:** Niemals vom Browser gesendete Preise, Gewichte oder Bestände als verlässliche Daten akzeptieren. Außerdem die Rechte serverseitig, das Escaping mit `e()`, die Validierung der Daten sowie das Fehlen von Secrets oder personenbezogenen Daten im öffentlichen HTML oder in einem gemeinsamen Cache prüfen.
8. **Nachweise:** den Positivtest „Fehlende, ausverkaufte und deaktivierte Varianten testen“ und den Ablehnungstest „Zwei Kombinationen erzeugen dieselbe SKU => ausdrückliche Ablehnung vor der Veröffentlichung“ schreiben. Regressionen bei SEO und Performance messen, den Rollback dokumentieren.
9. **Native Validierung:** `php tools/validate.php <dossier> --json`, `php tests/run.php` und `php tools/measure.php --check` auf einem offiziellen Checkout für jedes erzeugte Paket. Für einen vom Kern nicht unterstützten Teil einen Abweichungsvermerk und einen blockierenden Test liefern, niemals einen fiktiven Erfolg.

## Verpflichtende Liefergegenstände
- Mini-Spezifikation: Ziel, Benutzer, Abläufe, Zustände, Daten, Messungen.
- Berechtigungs- und Cache-Matrix: Route, Methode, Sitzung, Sichtbarkeit, Indexierung.
- Einstellungen und Inhalte, über die Administration oder als Entwurf über das MCP vorbereitet; **keine Erweiterung**, solange das Native genügt.
- Tests der Positivfälle und der Ablehnungen, Deaktivierungsverfahren, das die Daten erhält, Kompatibilitätsvermerk.

## Abnahmekriterien
- Fehlende, ausverkaufte und deaktivierte Varianten testen.
- Zwei Kombinationen erzeugen dieselbe SKU => ausdrückliche Ablehnung vor der Veröffentlichung.
- Nichts wird ohne eine autorisierte Person veröffentlicht, aktiviert oder in Produktion gebracht; kein Score, kein Ranking und keine Zitierung durch eine KI wird versprochen.
- Die von Éclair 2.0 nicht unterstützten Teile sind ausdrücklich als **nicht produktionsreif lieferbar** gekennzeichnet.

**Reifegrad dieses Skills:** `core-builtin-configuration-workflow`. Reproduzierbare Testfälle siehe `references/acceptance.md`.
