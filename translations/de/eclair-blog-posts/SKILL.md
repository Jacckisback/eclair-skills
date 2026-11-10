---
name: eclair-blog-posts
description: "Blogartikel mit dem nativen Block-Editor veröffentlichen und ordnen. Use on Éclair CMS 2.x when the user wants to: Blogartikel mit dem nativen Block-Editor veröffentlichen und ordnen. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Blogartikel — Éclair CMS 2.x

## Auslöser und erwartetes Ergebnis
Diesen Skill verwenden, um Folgendes zu erreichen: **Blogartikel mit dem nativen Block-Editor veröffentlichen und ordnen**. Diese Funktion ist **bereits in den Kern von Éclair 2.0 integriert**: Der Skill leitet ihre Konfiguration und Überprüfung an, ohne eine Erweiterung zu schreiben. Dieser Skill ist ein **Agenten-Workflow**, keine funktionsfähige PHP-Erweiterung und keine Konformitätsgarantie.

**WordPress-Entsprechung:** Native Beiträge von WordPress. Familie: Inhalte & Redaktion.

## Pflichtdiagnose vor jeder Änderung
1. `references/core-map.md` (was der Kern bereits leistet) und `references/native-contract.md` lesen; die tatsächliche Version des CMS und die Fähigkeiten in `GET /<admin>/api/capabilities` prüfen (sofern der Zugriff erlaubt ist).
2. `references/family-contract.md` und `references/acceptance.md` lesen. Niemals das alte Pack-System v0.x oder PHP-Code von WordPress in Éclair 2 kopieren.
3. Das Datenmodell ermitteln: **Artikel, Auszug, Hauptbild, Kategorie, Autor, Datum, Status Entwurf oder veröffentlicht**. Dokumentieren, was öffentlich ist, was privat ist und woher jede Angabe stammt.

## Spezifisches Vorgehen
4. **Ablauf:** Die Artikel über die Administration oder den MCP-Connector als Entwurf anlegen, Titel, Auszug, Bild und Kategorie prüfen, dann eine Person veröffentlichen lassen. Zustände und Fehler beschreiben, bevor Code geschrieben wird.
5. **Speicherorte:** websitespezifischer Code in `site/extensions/<id>/`, Erscheinungsbild in `site/themes/<id>/`, Daten unter `$ctx['data']`, Inhalte und Einstellungen über die Administration oder das MCP. Niemals `app/`, `assets/`, `index.php` oder den Updater bearbeiten.
6. **Aktueller Vertrag:** Die Funktion existiert im Kern: Sie über die Administration oder, als Entwurf, über den MCP-Connector einstellen. Sie nicht in einer Erweiterung duplizieren und niemals den Kern ändern, um sie anzupassen; geht ein Bedarf über das hinaus, was der Kern bietet, ihn als Lücke melden.
7. **Sicherheitsinvariante:** Niemals anstelle der berechtigten Person einen Inhalt veröffentlichen oder löschen. Außerdem die Rechte serverseitig, das Escaping mit `e()`, die Validierung der Daten sowie das Fehlen von Secrets oder personenbezogenen Daten im öffentlichen HTML oder in einem gemeinsamen Cache prüfen.
8. **Nachweise:** den Positivtest „Einen vollständigen Entwurf anlegen, ihn veröffentlichen lassen, dann Darstellung, RSS-Feed und Sitemap prüfen“ und den Ablehnungstest „Ein Entwurf erscheint weder auf der öffentlichen Website noch in der Sitemap noch im Feed“ schreiben. Regressionen bei SEO und Performance messen, den Rollback dokumentieren.
9. **Native Validierung:** `php tools/validate.php <dossier> --json`, `php tests/run.php` und `php tools/measure.php --check` auf einem offiziellen Checkout für jedes erzeugte Paket. Für einen vom Kern nicht unterstützten Teil einen Abweichungsvermerk und einen blockierenden Test liefern, niemals einen fiktiven Erfolg.

## Verpflichtende Liefergegenstände
- Mini-Spezifikation: Ziel, Benutzer, Abläufe, Zustände, Daten, Messungen.
- Berechtigungs- und Cache-Matrix: Route, Methode, Sitzung, Sichtbarkeit, Indexierung.
- Einstellungen und Inhalte, über die Administration oder als Entwurf über das MCP vorbereitet; **keine Erweiterung**, solange das Native genügt.
- Tests der Positivfälle und der Ablehnungen, Deaktivierungsverfahren, das die Daten erhält, Kompatibilitätsvermerk.

## Abnahmekriterien
- Einen vollständigen Entwurf anlegen, ihn veröffentlichen lassen, dann Darstellung, RSS-Feed und Sitemap prüfen.
- Ein Entwurf erscheint weder auf der öffentlichen Website noch in der Sitemap noch im Feed.
- Nichts wird ohne eine autorisierte Person veröffentlicht, aktiviert oder in Produktion gebracht; kein Score, kein Ranking und keine Zitierung durch eine KI wird versprochen.
- Die von Éclair 2.0 nicht unterstützten Teile sind ausdrücklich als **nicht produktionsreif lieferbar** gekennzeichnet.

**Reifegrad dieses Skills:** `core-builtin-configuration-workflow`. Reproduzierbare Testfälle siehe `references/acceptance.md`.
