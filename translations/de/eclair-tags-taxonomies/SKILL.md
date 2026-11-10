---
name: eclair-tags-taxonomies
description: "Schlagwörter oder eigene Taxonomien übernehmen, wenn der Kern nur Kategorien bietet. Use on Éclair CMS 2.x when the user wants to: Schlagwörter oder benutzerdefinierte Taxonomien übernehmen, wenn der Kern nur Kategorien bietet. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Schlagwörter und Taxonomien — Éclair CMS 2.x

## Auslöser und erwartetes Ergebnis
Diesen Skill verwenden, um Folgendes zu erreichen: **Schlagwörter oder benutzerdefinierte Taxonomien übernehmen, wenn der Kern nur Kategorien bietet**. Diese Funktion ist **teilweise durch den Vertrag des Kerns blockiert**: Der Skill liefert, was nativ ist, und dokumentiert die Lücke. Dieser Skill ist ein **Agenten-Workflow**, keine funktionsfähige PHP-Erweiterung und keine Konformitätsgarantie.

**WordPress-Entsprechung:** Schlagwörter und benutzerdefinierte Taxonomien von WordPress. Familie: Inhalte & Redaktion.

## Pflichtdiagnose vor jeder Änderung
1. `references/core-map.md` (was der Kern bereits leistet) und `references/native-contract.md` lesen; die tatsächliche Version des CMS und die Fähigkeiten in `GET /<admin>/api/capabilities` prüfen (sofern der Zugriff erlaubt ist).
2. `references/family-contract.md` und `references/acceptance.md` lesen. Niemals das alte Pack-System v0.x oder PHP-Code von WordPress in Éclair 2 kopieren.
3. Das Datenmodell ermitteln: **Begriff, Taxonomietyp, verknüpfte Inhalte, Archivadresse**. Dokumentieren, was öffentlich ist, was privat ist und woher jede Angabe stammt.

## Spezifisches Vorgehen
4. **Ablauf:** Die vorhandenen Taxonomien inventarisieren, diejenigen zusammenführen, die sich mit den Kategorien doppeln, für den Rest Sammelseiten per GET vorschlagen und die alten Archive weiterleiten. Zustände und Fehler beschreiben, bevor Code geschrieben wird.
5. **Speicherorte:** websitespezifischer Code in `site/extensions/<id>/`, Erscheinungsbild in `site/themes/<id>/`, Daten unter `$ctx['data']`, Inhalte und Einstellungen über die Administration oder das MCP. Niemals `app/`, `assets/`, `index.php` oder den Updater bearbeiten.
6. **Aktueller Vertrag:** Ein Teil hängt von einem Hook ab, der im Vertrag 2.0 fehlt (Inhaltstypen, SEO- oder JSON-LD-Beitrag, Inhaltsrichtlinie pro Erweiterung, Rendering-Filter). Den nativen Teil liefern und die Lücke präzise dokumentieren, ohne Workaround.
7. **Sicherheitsinvariante:** Keine Hunderte von dürftigen, indexierbaren Archiven erzeugen. Außerdem die Rechte serverseitig, das Escaping mit `e()`, die Validierung der Daten sowie das Fehlen von Secrets oder personenbezogenen Daten im öffentlichen HTML oder in einem gemeinsamen Cache prüfen.
8. **Nachweise:** den Positivtest „Einen Satz von Schlagwörtern in Kategorien oder Sammelseiten umwandeln und die Weiterleitungen prüfen“ und den Ablehnungstest „Ein altes, gelöschtes Schlagwortarchiv leitet ohne Kette auf die nächstliegende Seite weiter“ schreiben. Regressionen bei SEO und Performance messen, den Rollback dokumentieren.
9. **Native Validierung:** `php tools/validate.php <dossier> --json`, `php tests/run.php` und `php tools/measure.php --check` auf einem offiziellen Checkout für jedes erzeugte Paket. Für einen vom Kern nicht unterstützten Teil einen Abweichungsvermerk und einen blockierenden Test liefern, niemals einen fiktiven Erfolg.

## Verpflichtende Liefergegenstände
- Mini-Spezifikation: Ziel, Benutzer, Abläufe, Zustände, Daten, Messungen.
- Berechtigungs- und Cache-Matrix: Route, Methode, Sitzung, Sichtbarkeit, Indexierung.
- Paket oder Einstellungen für den nativen Teil und präziser Abweichungsvermerk für den blockierten Teil.
- Tests der Positivfälle und der Ablehnungen, Deaktivierungsverfahren, das die Daten erhält, Kompatibilitätsvermerk.

## Abnahmekriterien
- Einen Satz von Schlagwörtern in Kategorien oder Sammelseiten umwandeln und die Weiterleitungen prüfen.
- Ein altes, gelöschtes Schlagwortarchiv leitet ohne Kette auf die nächstliegende Seite weiter.
- Nichts wird ohne eine autorisierte Person veröffentlicht, aktiviert oder in Produktion gebracht; kein Score, kein Ranking und keine Zitierung durch eine KI wird versprochen.
- Die von Éclair 2.0 nicht unterstützten Teile sind ausdrücklich als **nicht produktionsreif lieferbar** gekennzeichnet.

**Reifegrad dieses Skills:** `partly-blocked-by-core-contract`. Reproduzierbare Testfälle siehe `references/acceptance.md`.
