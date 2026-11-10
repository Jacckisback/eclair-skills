---
name: eclair-cache-contract
description: Use when deciding Éclair CMS v2 static/uncached extension route behavior, invalidation, privacy and performance budgets.
---

# Éclair Cache Contract — den Cache sicher halten

## Entscheidung
1. `eclair/index.php`, `Cache.php`, `Extensions::route()` und `docs/EXTENSION-CONTRACT.md` des anvisierten Kerns v2 lesen.
2. Für Erweiterungsseiten mit öffentlichem, für alle identischem Inhalt kann `routes.public[].cache` nach Prüfung der Rendering-Abhängigkeiten `true` sein.
3. Für private Inhalte, Benutzerzustände, Warenkörbe, Token oder personalisierte Preise: **kein gemeinsamer Cache** (`Cache-Control: private, no-store`), passendes `noindex` und serverseitiger Authentifizierungsvertrag. Niemals vorgeben, dass ein `cache:false` für sich allein die Authentifizierung umsetzt.
4. GET/HEAD und Query-Strings, erste Generierung und danach Cache-HIT, Bearbeitung der Daten, Aktivierung/Deaktivierung und Migrationen messen. Die CMS-Routen und den Index `data/ext-public.php` prüfen.
5. Dem schnellen Pfad `index.php` niemals einen Lookup oder einen Registry-Lesezugriff hinzufügen, ohne gemessenes Budget und sicherheitsbezogene Begründung.
6. `php tools/measure.php --check` und die Budgets in `tools/budgets.json` testen, dann mit einer sauberen Baseline bei gleicher PHP-Version und gleichen Daten vergleichen.
7. Die Bereinigung nach der Aktivierung prüfen und dass nicht betroffene öffentliche Seiten cachefähig bleiben; Cookies und Header unter Nebenläufigkeit testen.

## Liefergegenstände
Matrix URL × Methode × Identität × Cache, Messungen und Isolationstests.

## V1.0 — Identität und Cache
Niemals eine personalisierte Seite aus einem gemeinsamen Cache ausliefern. Die bestehenden Administratorrouten sind bereits `private, no-store`; künftige öffentliche Mitgliederseiten erfordern vor jeder Öffnung einen Vertrag für private Routen. Niemals annehmen, dass `cache:false` automatisch vollständige Sitzungs-/CSRF-Garantien umsetzt.

## Éclair 2.0 — Prototyp v1.1 (experimentell)
Öffentliche GET-Formulare verwenden `Security::formField()` und müssen mit `cache:false` deklariert werden. Ihre Antworten dürfen den Fast Path des Kerns nicht erreichen. POST ist vom Fast Path ausgeschlossen und wird auf no-store gezwungen. Die Bereinigung des Caches bei der Aktivierung des Moduls testen und prüfen, dass im HTML des gemeinsamen Caches keine Cookies/Identitäten enthalten sind.

## Éclair 2.0 — Registrierung und Wiederherstellung (v1.2, experimentell)

`references/member-email-v1.2.md` vor jeder Anfrage zur Erstellung von Konten für Kunden/Lernende oder zur Passwortwiederherstellung lesen. Das Modul `member-directory` v0.3 verwendet öffentliche POST-Routen **außerhalb des offiziellen Vertrags**; niemals eine direkte Installation auf einem unveränderten Éclair 2.0 versprechen und die E-Mail-Abläufe nicht ohne verifizierte HTTPS-URL und native Tests aktivieren. Das Erweiterungssystem von v2 jeder Änderung an der alten v0.x-Architektur vorziehen. Öffentliche Konten und Administratorkonten getrennt halten, jeden gemeinsamen Cache für Mitgliederseiten ablehnen und E-Mails als nicht zugestellt behandeln, solange keine Bestätigung vorliegt.
