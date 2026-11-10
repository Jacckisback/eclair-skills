---
name: eclair-routing
description: Use when creating Éclair CMS 2.0 extension public/admin routes and maintaining exact URLs, redirects and WordPress SEO migration compatibility.
---

# Éclair Routing — URLs und Kompatibilität schützen

## Vorgehen
1. Die bestehenden Routen und Aliasse, `Site.php`, `App.php`, `Aliases.php`, `Redirects.php`, `Content::byRoute` und die reservierten URLs erfassen.
2. Die öffentlichen Erweiterungsrouten `routes.public[]` sind **nur GET** und ausdrücklich aufgezählt. Keine generische Route `/{slug}` über ein erfundenes Manifest.
3. Die Admin-Routen verwenden `routes.admin[]`, Methode GET/POST, unter `/<admin>/x/<id>/...` und mit dem nativen Recht `right`.
4. Vor der Aktivierung Kollisionen mit Artikeln/Seiten/Produkten, reservierten Routen, mehrsprachigem Slug, Website im Unterverzeichnis und anderen Erweiterungen testen.
5. Den exakten Pfad einer WordPress-Migration (abschließender Schrägstrich, .html, Akzente) über die v2-Mechanismen `route`/`Aliases` bewahren, ohne mehrere Canonicals oder 301-Kaskaden zu erzeugen.
6. Für eine Funktion, die öffentliche POST-Routen benötigt (Checkout, Kunden-API), ein RFC/eine neue gesicherte Schnittstelle dokumentieren, statt den Kern abzufangen oder den Router zu umgehen.
7. Canonicals, Sitemap, JSON-LD, noindex für private Oberflächen, `HEAD`, 404-/405-Antworten und Cache prüfen.

## Liefergegenstände
Routentabelle, Eigentümer des Namespace, Weiterleitungsplan, erkannte Konflikte und HTTP-Tests.

## V1.0 — Öffentliche Anmelderoute verboten
Die deklarativen öffentlichen GETs von Éclair 2.0 eignen sich für öffentliche Seiten, **nicht** für ein POST-Anmeldeformular. Keine Route `/login` oder `/register` mit Seiteneffekten darf mit GET erstellt werden. `member-directory` deklariert ausschließlich Admin-Routen mit dem Recht `users`.

## Éclair 2.0 — Prototyp v1.1 (experimentell)
Öffentliche POST-Routen sind im offiziellen Éclair 2.0 **nicht** vorhanden. Der vorgeschlagene Patch v1.1 macht eine kontrollierte Ausnahme: explizite Methode POST, `cache:false`, HTTPS, `Security::checkFormToken()`, Antwort `private,no-store`, relative 303-Weiterleitung. Vor dem Mergen immer HTTP-Tests mit dem vollständigen CMS durchführen.

## Éclair 2.0 — Registrierung und Wiederherstellung (v1.2, experimentell)

`references/member-email-v1.2.md` vor jeder Anfrage zur Erstellung von Konten für Kunden/Lernende oder zur Passwortwiederherstellung lesen. Das Modul `member-directory` v0.3 verwendet öffentliche POST-Routen **außerhalb des offiziellen Vertrags**; niemals eine direkte Installation auf einem unveränderten Éclair 2.0 versprechen und die E-Mail-Abläufe nicht ohne verifizierte HTTPS-URL und native Tests aktivieren. Das Erweiterungssystem von v2 jeder Änderung an der alten v0.x-Architektur vorziehen. Öffentliche Konten und Administratorkonten getrennt halten, jeden gemeinsamen Cache für Mitgliederseiten ablehnen und E-Mails als nicht zugestellt behandeln, solange keine Bestätigung vorliegt.
