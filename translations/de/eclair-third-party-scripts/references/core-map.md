# Éclair CMS 2.0.x — geprüfte Karte des Kerns

Referenz: öffentliches Repository `Jacckisback/eclair-cms`, Branch `main`, geprüft am 9. November 2026, Referenz-Commit `6567d7642ea2227a598c4988e970d43e2e5e0e4f`. **Ein Agent muss den tatsächlichen Checkout und `GET /<admin>/api/capabilities` stets erneut prüfen**: Diese Notiz ist eine Momentaufnahme, keine Garantie für künftige Kompatibilität.

## 1. Bereits in den Kern integriert: konfigurieren, nicht neu bauen

Vor dem Schreiben irgendeiner Erweiterung prüfen, ob der Bedarf nativ abgedeckt ist:

- **Inhalte**: Seiten und Artikel aus Blöcken, Kategorien, Menüs, Autoren, Entwürfe, Redaktionsplan; Blöcke `paragraph`, `heading`, `list`, `quote`, `image`, `video`, `table`, `code`, `button`, `callout`, `divider`, `hero`, `features`, `faq`, `team`, `contact`.
- **Medien**: Bilder werden skaliert, neu kodiert und in responsives WebP umgewandelt, explizite Abmessungen, verzögertes Laden.
- **Kontaktformular** und Posteingang für Nachrichten (Recht `messages`).
- **SEO und GEO**: Titel und Beschreibungen mit Live-Analyse, JSON-LD (Organisation oder lokales Unternehmen, Artikel, FAQ, Brotkrumenpfad), Sitemap mit Bildern und `hreflang`, RSS-Feed, Open Graph mit Vorschaubild zum Teilen, 301-Weiterleitungen und Weiterleitungsverwaltung, IndexNow, `llms.txt`, Markdown-Version jeder Seite, Richtlinie für KI-Crawler.
- **Geschwindigkeit**: statischer Cache jeder öffentlichen Seite, eingebettetes CSS, ein einziges öffentliches Skript, kein öffentliches Cookie.
- **Sicherheit**: Zwei-Faktor-Authentifizierung, Begrenzung der Versuche, strikte Content-Security-Policy, bereinigte Inhalte, Integritätsprüfung, Protokoll, signierte Updates mit Rollback.
- **Sicherungen**: Download und geplanter Versand an einen entfernten Speicher, Wiederherstellung.
- **Leichtgewichtiger Shop**: Produktseiten, Varianten, Kategorien, Zahlungslinks eines Anbieters, Händler-Feed; **kein Warenkorb, keine Bestellung und kein Kundenkonto**.
- **Mitgelieferte Funktionen**: Affiliate, Werbung, Planung, WordPress-Import, Übernahme einer alten Website, Nachverfolgung der KI-Crawler.
- **KI-Assistent und MCP-Connector**: nur Entwürfe und Vorschläge, niemals Veröffentlichung oder Löschung.
- **Erscheinungsbild**: Themes und Gestaltungsrichtungen, Vorschau vor dem Speichern.

## 2. Wo ein Skill schreiben darf

- Kern-Code: `eclair/app/`, `eclair/assets/`, `eclair/index.php` — **niemals bearbeiten**, um eine Website-Funktionalität zu liefern.
- Erweiterungen der Website: `site/extensions/<id>/` mit `extension.json`, `extension.php`, `lib/`, `assets/`, `lang/`.
- Themes der Website: `site/themes/<id>/` mit `theme.json`.
- Daten einer Erweiterung: `Eclair\Store`, Präfix `$ctx['data']` (`data/ext/<id>/`), Secrets in `data/ext/<id>/secrets.php`.
- Inhalte und Einstellungen: ausschließlich über die Administration oder den MCP-Connector.

## 3. Vertrag `eclair-extension/1`

- Öffentliche Routen einer Erweiterung: **nur GET**, im Manifest deklariert, cachefähig oder nicht.
- Administration: GET/POST unter `/<admin>/x/<id>/...`, Rechte des Kerns (`content`, `media`, `menus`, `categories`, `messages`, `redirects`, `settings`, `users`, `security`) und CSRF-Schutz.
- Deklarative, vom Kern validierte Blöcke und Einstellungen; geplante Aufgaben (höchstens einmal pro Stunde); idempotente Migrationen; veröffentlichte Assets.
- Der Code einer Erweiterung ist **vertrauenswürdig, ohne Sandbox**: Import und Aktivierung erfordern eine autorisierte Person.
- Validierung: `php tools/validate.php <dossier> --json`, dann `php tests/run.php` und `php tools/measure.php --check` in einem Checkout des Kerns.

## 4. Bekannte Grenzen der 2.0

- Keine öffentliche POST-Route für Erweiterungen (PR #19 im Entwurf, nicht gemergt), also keine Registrierung, kein Kommentar, keine Bestellung und kein Upload durch einen Besucher außerhalb des nativen Kontaktformulars.
- Keine öffentliche Identität (Kunde, Lernender, Mitglied) im nativen Vertrag.
- Kein erweiterungseigener Inhaltstyp; kein SEO- oder JSON-LD-Beitrag pro Erweiterung; keine Inhaltsrichtlinie (CSP) pro Erweiterung; kein allgemeiner Rendering-Filter.
- Schlagwörter, Kommentare und benutzerdefinierte Inhaltstypen von WordPress werden vom Import nicht übernommen.
- Die alten Prototypen Éclair Devkit v0.x zielten auf den Kern 1.14 und **gelten nicht** für die 2.0.

Offizielle Quellen:
- https://github.com/Jacckisback/eclair-cms/blob/main/docs/EXTENSION-CONTRACT.md
- https://github.com/Jacckisback/eclair-cms/blob/main/docs/THEME-CONTRACT.md
- https://github.com/Jacckisback/eclair-cms/blob/main/docs/SKILLS-GUIDE.md
- https://github.com/Jacckisback/eclair-cms/blob/main/docs/ARCHITECTURE-2.md
- https://github.com/Jacckisback/eclair-cms/blob/main/docs/schemas/extension.schema.json
