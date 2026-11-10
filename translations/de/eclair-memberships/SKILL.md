---
name: eclair-memberships
description: "Mitgliedschaftsstufen, Verlängerungen und Zugriffsrechte verwalten. Use on Éclair CMS 2.x when the user wants to: Mitgliedsstufen, Fälligkeiten und Zugriffsrechte verwalten. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Abonnements und Mitgliedschaften — Éclair CMS 2.x

## Auslöser und erwartetes Ergebnis
Diesen Skill verwenden, um Folgendes zu erreichen: **Mitgliedsstufen, Fälligkeiten und Zugriffsrechte verwalten**. Diese Funktion **erfordert Fähigkeiten, die im Kern 2.0 fehlen**: Der Skill liefert Konzeption, ein sicheres Mockup und Tests, keine Produktivsetzung. Dieser Skill ist ein **Agenten-Workflow**, keine funktionsfähige PHP-Erweiterung und keine Konformitätsgarantie.

**WordPress-Entsprechung:** MemberPress, Paid Memberships Pro. Familie: Business-Apps.

## Pflichtdiagnose vor jeder Änderung
1. `references/core-map.md` (was der Kern bereits leistet) und `references/native-contract.md` lesen; die tatsächliche Version des CMS und die Fähigkeiten in `GET /<admin>/api/capabilities` prüfen (sofern der Zugriff erlaubt ist).
2. `references/family-contract.md` und `references/acceptance.md` lesen. Niemals das alte Pack-System v0.x oder PHP-Code von WordPress in Éclair 2 kopieren.
3. Das Datenmodell ermitteln: **Tarif, Mitgliedschaft, Verlängerung, Zeitraum, Kündigung, Zahlung, Recht**. Dokumentieren, was öffentlich ist, was privat ist und woher jede Angabe stammt.

## Spezifisches Vorgehen
4. **Ablauf:** Rechte aus dem verifizierten Zustand berechnen, Tarifwechsel und Kulanzfristen vorsehen, Abrechnungsereignisse idempotent behandeln. Zustände und Fehler beschreiben, bevor Code geschrieben wird.
5. **Speicherorte:** websitespezifischer Code in `site/extensions/<id>/`, Erscheinungsbild in `site/themes/<id>/`, Daten unter `$ctx['data']`, Inhalte und Einstellungen über die Administration oder das MCP. Niemals `app/`, `assets/`, `index.php` oder den Updater bearbeiten.
6. **Aktueller Vertrag:** Öffentliche Schaufensterseiten sind mit GET möglich; Buchungen, Zahlungen, Bewerbungen, CRM und personenbezogene Daten erfordern gesichertes POST, geeigneten Speicher und serverseitig geprüfte Rechte.
7. **Sicherheitsinvariante:** Ein Beleg aus dem Browser genügt niemals, um einen kostenpflichtigen Zugriff zu verlängern. Außerdem die Rechte serverseitig, das Escaping mit `e()`, die Validierung der Daten sowie das Fehlen von Secrets oder personenbezogenen Daten im öffentlichen HTML oder in einem gemeinsamen Cache prüfen.
8. **Nachweise:** den Positivtest „Fehlgeschlagene Abbuchung, anteilige Berechnung, Erstattung und Kündigung testen“ und den Ablehnungstest „Zwei identische Ereignisse verlängern das Abonnement nicht zweimal“ schreiben. Regressionen bei SEO und Performance messen, den Rollback dokumentieren.
9. **Native Validierung:** `php tools/validate.php <dossier> --json`, `php tests/run.php` und `php tools/measure.php --check` auf einem offiziellen Checkout für jedes erzeugte Paket. Für einen vom Kern nicht unterstützten Teil einen Abweichungsvermerk und einen blockierenden Test liefern, niemals einen fiktiven Erfolg.

## Verpflichtende Liefergegenstände
- Mini-Spezifikation: Ziel, Benutzer, Abläufe, Zustände, Daten, Messungen.
- Berechtigungs- und Cache-Matrix: Route, Methode, Sitzung, Sichtbarkeit, Indexierung.
- Konzeptionsunterlagen, sicheres GET-Mockup falls sinnvoll, blockierende Tests und Anfrage zur Weiterentwicklung des Kerns; **kein Produktionspaket**.
- Tests der Positivfälle und der Ablehnungen, Deaktivierungsverfahren, das die Daten erhält, Kompatibilitätsvermerk.

## Abnahmekriterien
- Fehlgeschlagene Abbuchung, anteilige Berechnung, Erstattung und Kündigung testen.
- Zwei identische Ereignisse verlängern das Abonnement nicht zweimal.
- Nichts wird ohne eine autorisierte Person veröffentlicht, aktiviert oder in Produktion gebracht; kein Score, kein Ranking und keine Zitierung durch eine KI wird versprochen.
- Die von Éclair 2.0 nicht unterstützten Teile sind ausdrücklich als **nicht produktionsreif lieferbar** gekennzeichnet.

**Reifegrad dieses Skills:** `design-workflow-requires-verified-core-capabilities`. Reproduzierbare Testfälle siehe `references/acceptance.md`.
