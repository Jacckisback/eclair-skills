---
name: eclair-extension-builder
description: Use when creating or adapting an Éclair CMS 2.0 optional server extension that uses extension.json, extension.php and the native eclair-extension/1 contract.
---

# Éclair Extension Builder — eine in v2 wirklich installierbare Erweiterung bauen

## Ziel
Ein **mit dem Kern v2 konformes Paket `eclair-extension/1`** erstellen. Das Manifest `manifest.json` oder die Dateien `events.php` / `services.php` der alten Prototypen nicht so verwenden, als würden sie unterstützt.

## Vorgehen
1. `references/core-map.md`, `docs/EXTENSION-CONTRACT.md`, `docs/schemas/extension.schema.json` und `examples/extensions/bonjour` des Checkouts lesen.
2. `ECLAIR_VERSION` und den Vertrag `eclair-extension/1` anhand des Codes und, sofern zugänglich, über die API der Fähigkeiten prüfen.
3. `id`, `version`, `requires`, `depends`, `provides`, `entry`, Routen, Blöcke, Felder, Assets, `tasks`, Migrationen festlegen; ausschließlich die Felder des Schemas verwenden.
4. In `site/extensions/<id>/` ausliefern, **ohne in `app/` zu schreiben**; der PHP-Einstiegspunkt muss ein Objekt zurückgeben und darf beim Laden nichts ausgeben.
5. Die Ausgabe mit `e()` absichern; die Einstellungen aus `$ctx['settings']` lesen; über `Eclair\Store` unter `$ctx['data']` speichern. Für Secrets: privater Ablageort und dokumentierte Richtlinie zum Ausschluss aus Sicherungen.
6. Öffentliche Routen nur GET. Bei einer öffentlichen Seite, die Sitzungs- oder personenbezogene Daten anzeigt: abbrechen und einen neuen Identitäts-/Cache-Vertrag anfordern; keine vorgetäuschte Umgehung.
7. Die SHA-256-Werte der Dateien berechnen und in `files` deklarieren, außer für `extension.json`. Ein ZIP-Paket erzeugen, dessen Wurzel das Manifest enthält.
8. `php tools/validate.php chemin/extension --json`; alle Fehler beheben, bevor der Import vorgeschlagen wird, dann `php tests/run.php` und `php tools/measure.php --check` testen.
9. Eine autorisierte Person importiert, prüft in der Vorschau und aktiviert; die Deaktivierung, das Entfernen des Codes und die Aufbewahrung der Daten dokumentieren.

## Liefergegenstände
`extension.json`, Einstiegspunkt `extension.php`, Referenzen, Tests, Nachweis der offiziellen Validierung und Installationsanleitung. Originalbeispiel in `examples/extensions/skill-sample/`; vor dem Deployment auf dem exakten Kern prüfen.

## V1.0 — Ausgeliefertes fortgeschrittenes Muster
`examples/extensions/member-directory` ansehen: Es belegt native Admin-Routen GET/POST und eine PHP-Bibliothek, die nur von der Erweiterung geladen wird. Dessen Admin-GET nicht in eine öffentliche Anmeldung umwandeln und kein POST zu `routes.public` hinzufügen (mit dem Vertrag v2 inkompatibel).

## Éclair 2.0 — Prototyp v1.1 (experimentell)
Ein Prototyp einer öffentlichen POST-Route befindet sich in `examples/extensions/member-directory/`. Er wird vom offiziellen Kern 2.0 abgelehnt. Das Manifest nur mit dem experimentellen Patch und der ausdrücklichen Zustimmung eines Maintainers verwenden, niemals in Produktion. POST erfordert `cache:false`, TLS, CSRF und eine relative Weiterleitung.

## Éclair 2.0 — Registrierung und Wiederherstellung (v1.2, experimentell)

`references/member-email-v1.2.md` vor jeder Anfrage zur Erstellung von Konten für Kunden/Lernende oder zur Passwortwiederherstellung lesen. Das Modul `member-directory` v0.3 verwendet öffentliche POST-Routen **außerhalb des offiziellen Vertrags**; niemals eine direkte Installation auf einem unveränderten Éclair 2.0 versprechen und die E-Mail-Abläufe nicht ohne verifizierte HTTPS-URL und native Tests aktivieren. Das Erweiterungssystem von v2 jeder Änderung an der alten v0.x-Architektur vorziehen. Öffentliche Konten und Administratorkonten getrennt halten, jeden gemeinsamen Cache für Mitgliederseiten ablehnen und E-Mails als nicht zugestellt behandeln, solange keine Bestätigung vorliegt.
