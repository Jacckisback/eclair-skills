---
name: eclair-enrollment-access
description: "Einen Kauf oder eine Freigabe mit einer Einschreibung und deren Rechten verknüpfen. Use on Éclair CMS 2.x when the user wants to: Kauf oder Freigabe mit einer Einschreibung und ihren Berechtigungen verknüpfen. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Kurseinschreibungen — Éclair CMS 2.x

## Auslöser und erwartetes Ergebnis
Diesen Skill verwenden, um Folgendes zu erreichen: **Kauf oder Freigabe mit einer Einschreibung und ihren Berechtigungen verknüpfen**. Diese Funktion **erfordert Fähigkeiten, die im Kern 2.0 fehlen**: Der Skill liefert Konzeption, ein sicheres Mockup und Tests, keine Produktivsetzung. Dieser Skill ist ein **Agenten-Workflow**, keine funktionsfähige PHP-Erweiterung und keine Konformitätsgarantie.

**WordPress-Entsprechung:** Einschreibungen von LearnDash, MemberPress Courses. Familie: LMS.

## Pflichtdiagnose vor jeder Änderung
1. `references/core-map.md` (was der Kern bereits leistet) und `references/native-contract.md` lesen; die tatsächliche Version des CMS und die Fähigkeiten in `GET /<admin>/api/capabilities` prüfen (sofern der Zugriff erlaubt ist).
2. `references/family-contract.md` und `references/acceptance.md` lesen. Niemals das alte Pack-System v0.x oder PHP-Code von WordPress in Éclair 2 kopieren.
3. Das Datenmodell ermitteln: **Mitglied, Kurs, Einschreibung, Zustand, Herkunft, Datum und Widerruf**. Dokumentieren, was öffentlich ist, was privat ist und woher jede Angabe stammt.

## Spezifisches Vorgehen
4. **Ablauf:** Idempotente Einschreibung anlegen; Rechte je Objekt behandeln; kostenlose/kostenpflichtige Einschreibung unterscheiden; nach Erstattung gemäß ausdrücklicher Regel widerrufen. Zustände und Fehler beschreiben, bevor Code geschrieben wird.
5. **Speicherorte:** websitespezifischer Code in `site/extensions/<id>/`, Erscheinungsbild in `site/themes/<id>/`, Daten unter `$ctx['data']`, Inhalte und Einstellungen über die Administration oder das MCP. Niemals `app/`, `assets/`, `index.php` oder den Updater bearbeiten.
6. **Aktueller Vertrag:** Seiten zur Kursvorstellung können öffentlich per GET sein. Kostenpflichtige Kurse, Fortschritt und Bewertungen erfordern eine qualifizierte Mitgliederidentität, Zugriffsprüfungen auf Objektebene und private, nicht cachefähige Schreibvorgänge.
7. **Sicherheitsinvariante:** Niemals eine automatische Einschreibung allein aufgrund einer Rückkehr-URL des Zahlungsdienstleisters. Außerdem die Rechte serverseitig, das Escaping mit `e()`, die Validierung der Daten sowie das Fehlen von Secrets oder personenbezogenen Daten im öffentlichen HTML oder in einem gemeinsamen Cache prüfen.
8. **Nachweise:** den Positivtest „Doppelkauf, Erstattung, Sperrung des Kontos testen“ und den Ablehnungstest „Ein ausgeschlossenes Mitglied kann nicht mehr auf die zuvor freigegebenen Lektionen zugreifen“ schreiben. Regressionen bei SEO und Performance messen, den Rollback dokumentieren.
9. **Native Validierung:** `php tools/validate.php <dossier> --json`, `php tests/run.php` und `php tools/measure.php --check` auf einem offiziellen Checkout für jedes erzeugte Paket. Für einen vom Kern nicht unterstützten Teil einen Abweichungsvermerk und einen blockierenden Test liefern, niemals einen fiktiven Erfolg.

## Verpflichtende Liefergegenstände
- Mini-Spezifikation: Ziel, Benutzer, Abläufe, Zustände, Daten, Messungen.
- Berechtigungs- und Cache-Matrix: Route, Methode, Sitzung, Sichtbarkeit, Indexierung.
- Konzeptionsunterlagen, sicheres GET-Mockup falls sinnvoll, blockierende Tests und Anfrage zur Weiterentwicklung des Kerns; **kein Produktionspaket**.
- Tests der Positivfälle und der Ablehnungen, Deaktivierungsverfahren, das die Daten erhält, Kompatibilitätsvermerk.

## Abnahmekriterien
- Doppelkauf, Erstattung, Sperrung des Kontos testen.
- Ein ausgeschlossenes Mitglied kann nicht mehr auf die zuvor freigegebenen Lektionen zugreifen.
- Nichts wird ohne eine autorisierte Person veröffentlicht, aktiviert oder in Produktion gebracht; kein Score, kein Ranking und keine Zitierung durch eine KI wird versprochen.
- Die von Éclair 2.0 nicht unterstützten Teile sind ausdrücklich als **nicht produktionsreif lieferbar** gekennzeichnet.

**Reifegrad dieses Skills:** `design-workflow-requires-verified-core-capabilities`. Reproduzierbare Testfälle siehe `references/acceptance.md`.
