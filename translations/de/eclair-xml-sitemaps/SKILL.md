---
name: eclair-xml-sitemaps
description: "Die native Sitemap prüfen und bei Suchmaschinen einreichen. Use on Éclair CMS 2.x when the user wants to: die native Sitemap prüfen und bei den Suchmaschinen anmelden. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# XML-Sitemap — Éclair CMS 2.x

## Auslöser und erwartetes Ergebnis
Diesen Skill verwenden, um Folgendes zu erreichen: **die native Sitemap prüfen und bei den Suchmaschinen anmelden**. Diese Funktion ist **bereits in den Kern von Éclair 2.0 integriert**: Der Skill leitet ihre Konfiguration und Überprüfung an, ohne eine Erweiterung zu schreiben. Dieser Skill ist ein **Agenten-Workflow**, keine funktionsfähige PHP-Erweiterung und keine Konformitätsgarantie.

**WordPress-Entsprechung:** Sitemaps von Yoast, Google XML Sitemaps. Familie: SEO, GEO & Migration.

## Pflichtdiagnose vor jeder Änderung
1. `references/core-map.md` (was der Kern bereits leistet) und `references/native-contract.md` lesen; die tatsächliche Version des CMS und die Fähigkeiten in `GET /<admin>/api/capabilities` prüfen (sofern der Zugriff erlaubt ist).
2. `references/family-contract.md` und `references/acceptance.md` lesen. Niemals das alte Pack-System v0.x oder PHP-Code von WordPress in Éclair 2 kopieren.
3. Das Datenmodell ermitteln: **Sitemap-Einträge, Daten, Bilder, Sprachen**. Dokumentieren, was öffentlich ist, was privat ist und woher jede Angabe stammt.

## Spezifisches Vorgehen
4. **Ablauf:** Die vom Kern erzeugte Sitemap kontrollieren, sie in den Tools der Suchmaschinen anmelden, die Abdeckungsfehler überwachen. Zustände und Fehler beschreiben, bevor Code geschrieben wird.
5. **Speicherorte:** websitespezifischer Code in `site/extensions/<id>/`, Erscheinungsbild in `site/themes/<id>/`, Daten unter `$ctx['data']`, Inhalte und Einstellungen über die Administration oder das MCP. Niemals `app/`, `assets/`, `index.php` oder den Updater bearbeiten.
6. **Aktueller Vertrag:** Die Funktion existiert im Kern: Sie über die Administration oder, als Entwurf, über den MCP-Connector einstellen. Sie nicht in einer Erweiterung duplizieren und niemals den Kern ändern, um sie anzupassen; geht ein Bedarf über das hinaus, was der Kern bietet, ihn als Lücke melden.
7. **Sicherheitsinvariante:** Die Sitemap listet nur veröffentlichte und indexierbare Seiten auf. Außerdem die Rechte serverseitig, das Escaping mit `e()`, die Validierung der Daten sowie das Fehlen von Secrets oder personenbezogenen Daten im öffentlichen HTML oder in einem gemeinsamen Cache prüfen.
8. **Nachweise:** den Positivtest „Die Sitemap validieren und mit der Anzahl der veröffentlichten Seiten vergleichen“ und den Ablehnungstest „Eine Seite im Entwurf oder eine weitergeleitete Seite steht nicht darin“ schreiben. Regressionen bei SEO und Performance messen, den Rollback dokumentieren.
9. **Native Validierung:** `php tools/validate.php <dossier> --json`, `php tests/run.php` und `php tools/measure.php --check` auf einem offiziellen Checkout für jedes erzeugte Paket. Für einen vom Kern nicht unterstützten Teil einen Abweichungsvermerk und einen blockierenden Test liefern, niemals einen fiktiven Erfolg.

## Verpflichtende Liefergegenstände
- Mini-Spezifikation: Ziel, Benutzer, Abläufe, Zustände, Daten, Messungen.
- Berechtigungs- und Cache-Matrix: Route, Methode, Sitzung, Sichtbarkeit, Indexierung.
- Einstellungen und Inhalte, über die Administration oder als Entwurf über das MCP vorbereitet; **keine Erweiterung**, solange das Native genügt.
- Tests der Positivfälle und der Ablehnungen, Deaktivierungsverfahren, das die Daten erhält, Kompatibilitätsvermerk.

## Abnahmekriterien
- Die Sitemap validieren und mit der Anzahl der veröffentlichten Seiten vergleichen.
- Eine Seite im Entwurf oder eine weitergeleitete Seite steht nicht darin.
- Nichts wird ohne eine autorisierte Person veröffentlicht, aktiviert oder in Produktion gebracht; kein Score, kein Ranking und keine Zitierung durch eine KI wird versprochen.
- Die von Éclair 2.0 nicht unterstützten Teile sind ausdrücklich als **nicht produktionsreif lieferbar** gekennzeichnet.

**Reifegrad dieses Skills:** `core-builtin-configuration-workflow`. Reproduzierbare Testfälle siehe `references/acceptance.md`.
