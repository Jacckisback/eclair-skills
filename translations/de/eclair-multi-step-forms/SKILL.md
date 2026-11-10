---
name: eclair-multi-step-forms
description: "Ein langes Formular in Schritten konzipieren. Use on Éclair CMS 2.x when the user wants to: ein langes, in Schritte unterteiltes Formular konzipieren. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Mehrstufige Formulare — Éclair CMS 2.x

## Auslöser und erwartetes Ergebnis
Diesen Skill verwenden, um Folgendes zu erreichen: **ein langes, in Schritte unterteiltes Formular konzipieren**. Diese Funktion **erfordert Fähigkeiten, die im Kern 2.0 fehlen**: Der Skill liefert Konzeption, ein sicheres Mockup und Tests, keine Produktivsetzung. Dieser Skill ist ein **Agenten-Workflow**, keine funktionsfähige PHP-Erweiterung und keine Konformitätsgarantie.

**WordPress-Entsprechung:** Gravity Forms, Formidable Forms. Familie: Formulare.

## Pflichtdiagnose vor jeder Änderung
1. `references/core-map.md` (was der Kern bereits leistet) und `references/native-contract.md` lesen; die tatsächliche Version des CMS und die Fähigkeiten in `GET /<admin>/api/capabilities` prüfen (sofern der Zugriff erlaubt ist).
2. `references/family-contract.md` und `references/acceptance.md` lesen. Niemals das alte Pack-System v0.x oder PHP-Code von WordPress in Éclair 2 kopieren.
3. Das Datenmodell ermitteln: **Schritt, Felder, Validierung, Antwortentwurf**. Dokumentieren, was öffentlich ist, was privat ist und woher jede Angabe stammt.

## Spezifisches Vorgehen
4. **Ablauf:** Nach Themen unterteilen, bei jedem Schritt serverseitig validieren, Wiederaufnahme und Zusammenfassung vor dem Absenden vorsehen. Zustände und Fehler beschreiben, bevor Code geschrieben wird.
5. **Speicherorte:** websitespezifischer Code in `site/extensions/<id>/`, Erscheinungsbild in `site/themes/<id>/`, Daten unter `$ctx['data']`, Inhalte und Einstellungen über die Administration oder das MCP. Niemals `app/`, `assets/`, `index.php` oder den Updater bearbeiten.
6. **Aktueller Vertrag:** Diese Funktion verlangt Schreibvorgänge von Besuchern, öffentliche Konten, Transaktionen oder signierte Ereignisse, die `eclair-extension/1` in 2.0 nicht bereitstellt. Die Konzeption, ein sicheres GET-Mockup und blockierende Tests liefern; niemals eine Produktivsetzung ankündigen.
7. **Sicherheitsinvariante:** Keine Teildaten werden gespeichert, ohne die Person zu informieren. Außerdem die Rechte serverseitig, das Escaping mit `e()`, die Validierung der Daten sowie das Fehlen von Secrets oder personenbezogenen Daten im öffentlichen HTML oder in einem gemeinsamen Cache prüfen.
8. **Nachweise:** den Positivtest „Ausfüllen, zurückgehen, korrigieren und absenden“ und den Ablehnungstest „Ein ungültiger Schritt blockiert den weiteren Ablauf und keine unvollständigen Daten werden übermittelt“ schreiben. Regressionen bei SEO und Performance messen, den Rollback dokumentieren.
9. **Native Validierung:** `php tools/validate.php <dossier> --json`, `php tests/run.php` und `php tools/measure.php --check` auf einem offiziellen Checkout für jedes erzeugte Paket. Für einen vom Kern nicht unterstützten Teil einen Abweichungsvermerk und einen blockierenden Test liefern, niemals einen fiktiven Erfolg.

## Verpflichtende Liefergegenstände
- Mini-Spezifikation: Ziel, Benutzer, Abläufe, Zustände, Daten, Messungen.
- Berechtigungs- und Cache-Matrix: Route, Methode, Sitzung, Sichtbarkeit, Indexierung.
- Konzeptionsunterlagen, sicheres GET-Mockup falls sinnvoll, blockierende Tests und Anfrage zur Weiterentwicklung des Kerns; **kein Produktionspaket**.
- Tests der Positivfälle und der Ablehnungen, Deaktivierungsverfahren, das die Daten erhält, Kompatibilitätsvermerk.

## Abnahmekriterien
- Ausfüllen, zurückgehen, korrigieren und absenden.
- Ein ungültiger Schritt blockiert den weiteren Ablauf und keine unvollständigen Daten werden übermittelt.
- Nichts wird ohne eine autorisierte Person veröffentlicht, aktiviert oder in Produktion gebracht; kein Score, kein Ranking und keine Zitierung durch eine KI wird versprochen.
- Die von Éclair 2.0 nicht unterstützten Teile sind ausdrücklich als **nicht produktionsreif lieferbar** gekennzeichnet.

**Reifegrad dieses Skills:** `design-workflow-requires-verified-core-capabilities`. Reproduzierbare Testfälle siehe `references/acceptance.md`.
