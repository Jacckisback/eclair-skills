---
name: eclair-architecture
description: Use for Éclair CMS v2 architecture decisions, reviewing system boundaries and choosing whether a feature belongs to native settings, a theme, an extension or an isolated core RFC.
---

# Éclair Architecture — den Kern v2 bewahren

## Ziel
Die angeforderte Lösung entwerfen, **ohne ein Erweiterungssystem nachzubauen** und ohne die Cache-Route zu überladen. Mit `references/core-map.md` und dem Code des aktuellen Checkouts beginnen.

## Operativer Ablauf
1. Den Commit, die Version `ECLAIR_VERSION`, PHP und die verfügbaren Fähigkeiten über `/admin/api/capabilities` erfassen, sofern der Zugriff erlaubt ist.
2. Das Ziel einordnen: nativer Inhalt/native Einstellung, Site-Theme, Erweiterung `eclair-extension/1`, externer Dienst oder Lücke im öffentlichen Vertrag, die ein RFC erfordert.
3. Zuerst nach `Extensions`, `Themes`, `Packages`, `Migrations`, `Store`, `Cache`, `Site`, `Seo`, `Security`, `Mcp` und in den Dokumenten `docs/ARCHITECTURE-2.md`/`docs/STATUS-2.md` suchen.
4. Die Grenzen beschreiben: Code unter `site/extensions/` oder `site/themes/`, Daten über `Store` und `$ctx['data']`, Medien unter `media/`, kein Ersetzen von `app/`.
5. Den nativen Vertrag (`eclair-extension/1`) strikt von den alten v0.8-Experimenten (Routen/Berechtigungen/SQL/Outbox) unterscheiden, die ohne Portierung mit v2 inkompatibel sind.
6. Eine explizite Architekturentscheidung erstellen: Alternativen, Grenzen der API, Risiken, Rollback, Kompatibilitätstest und Leistungsindikatoren.
7. Gegenlesen lassen, dann mit `php tests/run.php`, `php tools/measure.php --check` und den relevanten Tests aus `tests/extensions.php` validieren.

## Nicht verhandelbar
SEO/GEO, Canonical-Auszeichnung, CSRF-/CSP-Schutz, Auth-Verwaltung und warmen Cache bewahren. Eine Erweiterung aktiviert sich niemals selbst. Weder vorgeben, einen transaktionalen Checkout zu verwalten, noch Konten für Lernende, solange diese Verträge nicht implementiert und getestet sind.

## Liefergegenstände
ADR und Kartierung vorher/nachher, Entscheidung „native / extension / core RFC“, Einschränkungen, Tests und Rollback-Plan. Die Vorlage `assets/architecture-decision.md` kann als Ausgangspunkt dienen.

## V1.0 — Mitglieder-Erweiterungen
Die native Erweiterung `examples/extensions/member-directory` veranschaulicht getrennte öffentliche Konten: keine neue Rolle in `Eclair\Users`. Ein Kern 2.0 nimmt Erweiterungen über `site/extensions/<id>` auf; kein Schreiben in `app/`.

## Éclair 2.0 — Prototyp v1.1 (experimentell)
Éclair 2.0.0 verfügt inzwischen über einen experimentellen Vertrag für öffentliche POST-Anfragen, jedoch nur, wenn der Patch v1.1 auf einem Entwicklungszweig angewendet ist. Der offizielle Kern stellt diesen Vertrag **nicht** bereit. Keine direkte Änderung des Kerns aus einem Skill heraus; ein RFC vorbereiten und vorab testen.

## Éclair 2.0 — Registrierung und Wiederherstellung (v1.2, experimentell)

`references/member-email-v1.2.md` vor jeder Anfrage zur Erstellung von Konten für Kunden/Lernende oder zur Passwortwiederherstellung lesen. Das Modul `member-directory` v0.3 verwendet öffentliche POST-Routen **außerhalb des offiziellen Vertrags**; niemals eine direkte Installation auf einem unveränderten Éclair 2.0 versprechen und die E-Mail-Abläufe nicht ohne verifizierte HTTPS-URL und native Tests aktivieren. Das Erweiterungssystem von v2 jeder Änderung an der alten v0.x-Architektur vorziehen. Öffentliche Konten und Administratorkonten getrennt halten, jeden gemeinsamen Cache für Mitgliederseiten ablehnen und E-Mails als nicht zugestellt behandeln, solange keine Bestätigung vorliegt.
