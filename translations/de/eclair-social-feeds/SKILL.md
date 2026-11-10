---
name: eclair-social-feeds
description: "Die neuesten Social-Media-Beiträge zeigen, ohne die Website zu beschweren. Use on Éclair CMS 2.x when the user wants to: die eigenen neuesten Social-Media-Beiträge anzeigen, ohne die Website zu beschweren. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Social-Media-Feeds — Éclair CMS 2.x

## Auslöser und erwartetes Ergebnis
Diesen Skill verwenden, um Folgendes zu erreichen: **die eigenen neuesten Social-Media-Beiträge anzeigen, ohne die Website zu beschweren**. Diese Funktion ist **teilweise durch den Vertrag des Kerns blockiert**: Der Skill liefert, was nativ ist, und dokumentiert die Lücke. Dieser Skill ist ein **Agenten-Workflow**, keine funktionsfähige PHP-Erweiterung und keine Konformitätsgarantie.

**WordPress-Entsprechung:** Smash Balloon, Instagram-Feeds. Familie: Marketing & Reichweite.

## Pflichtdiagnose vor jeder Änderung
1. `references/core-map.md` (was der Kern bereits leistet) und `references/native-contract.md` lesen; die tatsächliche Version des CMS und die Fähigkeiten in `GET /<admin>/api/capabilities` prüfen (sofern der Zugriff erlaubt ist).
2. `references/family-contract.md` und `references/acceptance.md` lesen. Niemals das alte Pack-System v0.x oder PHP-Code von WordPress in Éclair 2 kopieren.
3. Das Datenmodell ermitteln: **Beitrag, Bild, Link, Abrufdatum**. Dokumentieren, was öffentlich ist, was privat ist und woher jede Angabe stammt.

## Spezifisches Vorgehen
4. **Ablauf:** Die Beiträge per geplanter Aufgabe serverseitig abrufen, wenn das Netzwerk es erlaubt, sie als statisches HTML ausgeben; andernfalls einfache Links zu den Profilen. Zustände und Fehler beschreiben, bevor Code geschrieben wird.
5. **Speicherorte:** websitespezifischer Code in `site/extensions/<id>/`, Erscheinungsbild in `site/themes/<id>/`, Daten unter `$ctx['data']`, Inhalte und Einstellungen über die Administration oder das MCP. Niemals `app/`, `assets/`, `index.php` oder den Updater bearbeiten.
6. **Aktueller Vertrag:** Ein Teil hängt von einem Hook ab, der im Vertrag 2.0 fehlt (Inhaltstypen, SEO- oder JSON-LD-Beitrag, Inhaltsrichtlinie pro Erweiterung, Rendering-Filter). Den nativen Teil liefern und die Lücke präzise dokumentieren, ohne Workaround.
7. **Sicherheitsinvariante:** Kein Drittanbieter-Widget wird im Browser der Besucher geladen. Außerdem die Rechte serverseitig, das Escaping mit `e()`, die Validierung der Daten sowie das Fehlen von Secrets oder personenbezogenen Daten im öffentlichen HTML oder in einem gemeinsamen Cache prüfen.
8. **Nachweise:** den Positivtest „Die statische Ausgabe und die Aktualisierung per Aufgabe prüfen“ und den Ablehnungstest „Ist das Netzwerk nicht erreichbar, bleibt die letzte gültige Version angezeigt“ schreiben. Regressionen bei SEO und Performance messen, den Rollback dokumentieren.
9. **Native Validierung:** `php tools/validate.php <dossier> --json`, `php tests/run.php` und `php tools/measure.php --check` auf einem offiziellen Checkout für jedes erzeugte Paket. Für einen vom Kern nicht unterstützten Teil einen Abweichungsvermerk und einen blockierenden Test liefern, niemals einen fiktiven Erfolg.

## Verpflichtende Liefergegenstände
- Mini-Spezifikation: Ziel, Benutzer, Abläufe, Zustände, Daten, Messungen.
- Berechtigungs- und Cache-Matrix: Route, Methode, Sitzung, Sichtbarkeit, Indexierung.
- Paket oder Einstellungen für den nativen Teil und präziser Abweichungsvermerk für den blockierten Teil.
- Tests der Positivfälle und der Ablehnungen, Deaktivierungsverfahren, das die Daten erhält, Kompatibilitätsvermerk.

## Abnahmekriterien
- Die statische Ausgabe und die Aktualisierung per Aufgabe prüfen.
- Ist das Netzwerk nicht erreichbar, bleibt die letzte gültige Version angezeigt.
- Nichts wird ohne eine autorisierte Person veröffentlicht, aktiviert oder in Produktion gebracht; kein Score, kein Ranking und keine Zitierung durch eine KI wird versprochen.
- Die von Éclair 2.0 nicht unterstützten Teile sind ausdrücklich als **nicht produktionsreif lieferbar** gekennzeichnet.

**Reifegrad dieses Skills:** `partly-blocked-by-core-contract`. Reproduzierbare Testfälle siehe `references/acceptance.md`.
