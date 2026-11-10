---
name: eclair-automation-platforms
description: "Die Website mit Make, Zapier oder n8n verbinden. Use on Éclair CMS 2.x when the user wants to: die Website an Make, Zapier oder n8n anbinden. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Automatisierungsplattformen — Éclair CMS 2.x

## Auslöser und erwartetes Ergebnis
Diesen Skill verwenden, um Folgendes zu erreichen: **die Website an Make, Zapier oder n8n anbinden**. Der **öffentliche Leseteil ist heute umsetzbar**; Schreibvorgänge durch Besucher erfordern mehr als der aktuelle Vertrag. Dieser Skill ist ein **Agenten-Workflow**, keine funktionsfähige PHP-Erweiterung und keine Konformitätsgarantie.

**WordPress-Entsprechung:** Zapier for WordPress, Uncanny Automator. Familie: Integrationen & Automatisierung.

## Pflichtdiagnose vor jeder Änderung
1. `references/core-map.md` (was der Kern bereits leistet) und `references/native-contract.md` lesen; die tatsächliche Version des CMS und die Fähigkeiten in `GET /<admin>/api/capabilities` prüfen (sofern der Zugriff erlaubt ist).
2. `references/family-contract.md` und `references/acceptance.md` lesen. Niemals das alte Pack-System v0.x oder PHP-Code von WordPress in Éclair 2 kopieren.
3. Das Datenmodell ermitteln: **Szenario, Auslöser, übermittelte Daten**. Dokumentieren, was öffentlich ist, was privat ist und woher jede Angabe stammt.

## Spezifisches Vorgehen
4. **Ablauf:** Lesend bereitstellen, was die Plattform abfragen kann (Feeds, öffentliches JSON); den Empfang von Ereignissen für später konzipieren. Zustände und Fehler beschreiben, bevor Code geschrieben wird.
5. **Speicherorte:** websitespezifischer Code in `site/extensions/<id>/`, Erscheinungsbild in `site/themes/<id>/`, Daten unter `$ctx['data']`, Inhalte und Einstellungen über die Administration oder das MCP. Niemals `app/`, `assets/`, `index.php` oder den Updater bearbeiten.
6. **Aktueller Vertrag:** Das öffentliche Lesen (GET, cachefähig) ist heute umsetzbar. Jeder Schreibvorgang durch einen Besucher erfordert eine öffentliche POST-Route, die der Kern 2.0 für Erweiterungen nicht öffnet (PR #19 im Entwurf, nicht gemergt): sie nicht simulieren.
7. **Sicherheitsinvariante:** Keine personenbezogenen Daten werden in einem öffentlichen Endpunkt offengelegt, um eine Automatisierung zu erleichtern. Außerdem die Rechte serverseitig, das Escaping mit `e()`, die Validierung der Daten sowie das Fehlen von Secrets oder personenbezogenen Daten im öffentlichen HTML oder in einem gemeinsamen Cache prüfen.
8. **Nachweise:** den Positivtest „Einen öffentlichen Feed von der Plattform lesen lassen und ein Szenario auslösen“ und den Ablehnungstest „Ein nicht authentifizierter eingehender Aufruf ändert nichts an der Website“ schreiben. Regressionen bei SEO und Performance messen, den Rollback dokumentieren.
9. **Native Validierung:** `php tools/validate.php <dossier> --json`, `php tests/run.php` und `php tools/measure.php --check` auf einem offiziellen Checkout für jedes erzeugte Paket. Für einen vom Kern nicht unterstützten Teil einen Abweichungsvermerk und einen blockierenden Test liefern, niemals einen fiktiven Erfolg.

## Verpflichtende Liefergegenstände
- Mini-Spezifikation: Ziel, Benutzer, Abläufe, Zustände, Daten, Messungen.
- Berechtigungs- und Cache-Matrix: Route, Methode, Sitzung, Sichtbarkeit, Indexierung.
- Validiertes Nur-Lese-Paket (GET-Routen) und schriftlicher Plan für den Schreibteil, klar als nicht geliefert gekennzeichnet.
- Tests der Positivfälle und der Ablehnungen, Deaktivierungsverfahren, das die Daten erhält, Kompatibilitätsvermerk.

## Abnahmekriterien
- Einen öffentlichen Feed von der Plattform lesen lassen und ein Szenario auslösen.
- Ein nicht authentifizierter eingehender Aufruf ändert nichts an der Website.
- Nichts wird ohne eine autorisierte Person veröffentlicht, aktiviert oder in Produktion gebracht; kein Score, kein Ranking und keine Zitierung durch eine KI wird versprochen.
- Die von Éclair 2.0 nicht unterstützten Teile sind ausdrücklich als **nicht produktionsreif lieferbar** gekennzeichnet.

**Reifegrad dieses Skills:** `public-read-only-prototype-possible`. Reproduzierbare Testfälle siehe `references/acceptance.md`.
