---
name: eclair-maps-embeds
description: "Eine Anfahrtskarte zeigen, ohne Besucher zu tracken. Use on Éclair CMS 2.x when the user wants to: einen Anfahrtsplan anzeigen, ohne die Besucher zu tracken. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Karten und Anfahrtspläne — Éclair CMS 2.x

## Auslöser und erwartetes Ergebnis
Diesen Skill verwenden, um Folgendes zu erreichen: **einen Anfahrtsplan anzeigen, ohne die Besucher zu tracken**. Diese Funktion ist **teilweise durch den Vertrag des Kerns blockiert**: Der Skill liefert, was nativ ist, und dokumentiert die Lücke. Dieser Skill ist ein **Agenten-Workflow**, keine funktionsfähige PHP-Erweiterung und keine Konformitätsgarantie.

**WordPress-Entsprechung:** Google-Maps-Erweiterungen, Leaflet Map. Familie: Integrationen & Automatisierung.

## Pflichtdiagnose vor jeder Änderung
1. `references/core-map.md` (was der Kern bereits leistet) und `references/native-contract.md` lesen; die tatsächliche Version des CMS und die Fähigkeiten in `GET /<admin>/api/capabilities` prüfen (sofern der Zugriff erlaubt ist).
2. `references/family-contract.md` und `references/acceptance.md` lesen. Niemals das alte Pack-System v0.x oder PHP-Code von WordPress in Éclair 2 kopieren.
3. Das Datenmodell ermitteln: **Adresse, Koordinaten, Kartenbild, Routenlink**. Dokumentieren, was öffentlich ist, was privat ist und woher jede Angabe stammt.

## Spezifisches Vorgehen
4. **Ablauf:** Ein statisches Kartenbild mit Link zur Route bevorzugen; eine interaktive Karte eines Drittanbieters hängt von der nativen Inhaltsrichtlinie ab. Zustände und Fehler beschreiben, bevor Code geschrieben wird.
5. **Speicherorte:** websitespezifischer Code in `site/extensions/<id>/`, Erscheinungsbild in `site/themes/<id>/`, Daten unter `$ctx['data']`, Inhalte und Einstellungen über die Administration oder das MCP. Niemals `app/`, `assets/`, `index.php` oder den Updater bearbeiten.
6. **Aktueller Vertrag:** Ein Teil hängt von einem Hook ab, der im Vertrag 2.0 fehlt (Inhaltstypen, SEO- oder JSON-LD-Beitrag, Inhaltsrichtlinie pro Erweiterung, Rendering-Filter). Den nativen Teil liefern und die Lücke präzise dokumentieren, ohne Workaround.
7. **Sicherheitsinvariante:** Keine Karte eines Drittanbieters wird vor einer Aktion des Besuchers geladen. Außerdem die Rechte serverseitig, das Escaping mit `e()`, die Validierung der Daten sowie das Fehlen von Secrets oder personenbezogenen Daten im öffentlichen HTML oder in einem gemeinsamen Cache prüfen.
8. **Nachweise:** den Positivtest „Bild, Alternativtext und Routenlink auf dem Mobilgerät prüfen“ und den Ablehnungstest „Keine Anfrage an einen Kartendienst beim Laden der Seite“ schreiben. Regressionen bei SEO und Performance messen, den Rollback dokumentieren.
9. **Native Validierung:** `php tools/validate.php <dossier> --json`, `php tests/run.php` und `php tools/measure.php --check` auf einem offiziellen Checkout für jedes erzeugte Paket. Für einen vom Kern nicht unterstützten Teil einen Abweichungsvermerk und einen blockierenden Test liefern, niemals einen fiktiven Erfolg.

## Verpflichtende Liefergegenstände
- Mini-Spezifikation: Ziel, Benutzer, Abläufe, Zustände, Daten, Messungen.
- Berechtigungs- und Cache-Matrix: Route, Methode, Sitzung, Sichtbarkeit, Indexierung.
- Paket oder Einstellungen für den nativen Teil und präziser Abweichungsvermerk für den blockierten Teil.
- Tests der Positivfälle und der Ablehnungen, Deaktivierungsverfahren, das die Daten erhält, Kompatibilitätsvermerk.

## Abnahmekriterien
- Bild, Alternativtext und Routenlink auf dem Mobilgerät prüfen.
- Keine Anfrage an einen Kartendienst beim Laden der Seite.
- Nichts wird ohne eine autorisierte Person veröffentlicht, aktiviert oder in Produktion gebracht; kein Score, kein Ranking und keine Zitierung durch eine KI wird versprochen.
- Die von Éclair 2.0 nicht unterstützten Teile sind ausdrücklich als **nicht produktionsreif lieferbar** gekennzeichnet.

**Reifegrad dieses Skills:** `partly-blocked-by-core-contract`. Reproduzierbare Testfälle siehe `references/acceptance.md`.
