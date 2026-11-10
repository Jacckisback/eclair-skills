---
name: eclair-security-audit
description: Use when auditing Éclair CMS 2.0 native extensions, package supply chain, admin actions, member data and future commerce/LMS security.
---

# Éclair Security Audit — Prüfung vor der Aktivierung

## Umfang
1. Die Version des Kerns, die Herkunft der Erweiterung, die ausführbaren Dateien und die beanspruchten Berechtigungen feststellen.
2. Den konformen Vertrag `extension.json` und SHA-256-Prüfsummen für die Dateien verlangen; Symlinks, Path-Traversal-Pfade, unvorhergesehene Skripte, ZIP-Bomben, Größen, Methoden und reservierte Routen prüfen.
3. Das native `right` der Admin-Route und die fachlichen Autorisierungen auf den Objekten getrennt kontrollieren; ein Recht `content` berechtigt nicht dazu, die Bestellung eines anderen Kunden zu lesen.
4. CSRF, Rate Limiting, Session Fixation, direkten Dateizugriff, XSS im zurückgegebenen HTML, SQL-Injection, SSRF bei externen URLs und den Umgang mit Secrets testen.
5. Öffentliche Seiten mit `cache:true`: keine personenbezogenen Daten und keine Varianten pro Benutzer. Admin-Seiten: Header, Authentifizierung und Ablehnung als Standard.
6. Für einen Checkout: signierter Webhook mit serverseitiger Prüfung, Idempotenz, Beträge, Währung, Mehrwertsteuer und transaktionale Zustandsübergänge vor der Auslieferung.
7. Für Geschäftsereignisse: daran erinnern, dass v2 keinen Standard-Bus/keine Standard-Outbox enthält; separates Projekt mit Ausfalltests und ohne jedes Versprechen von exactly-once für entfernte Effekte.
8. Niemals nicht auditierte Module mit dem Vertrauen des PHP-Prozesses ausführen.

## Mindestnachweise
`php tools/validate.php chemin/extension --json`, `php tests/run.php`, `php tools/measure.php --check` und negative HTTP-Szenarien auf einer Testinstallation. Kein Sicherheitsbericht ist eine automatische Zertifizierung.

## Liefergegenstände
Liste der eingestuften Risiken, reproduzierbare Demonstrationen, Korrekturen, verbleibende Grenzen und ausdrückliche Go/No-Go-Entscheidung.

## V1.0 — Tests der Identität
Den Prototyp `member-directory` auditieren: kein Mitgliederkonto in `data/users.php`, Passwort niemals zurückgegeben, Status `pending` als Standard, Rollen `admin/editor` verboten, Widerrufs-Epoch, Objektkontrolle eigenes/fremdes Objekt, Cookie `__Host-` über HTTPS. Lokale Tests ersetzen kein Audit in Produktion.

## Éclair 2.0 — Prototyp v1.1 (experimentell)
Der Prototyp v1.1 hat eine Begrenzung per `RateLimit::attempt` vor dem Hashing, eine strikte Trennung zwischen Mitgliedern und Admins sowie Sitzungstoken mit 256 Bit. Die Sicherheit von `Origin`, von TLS hinter einem Reverse Proxy, CSRF, IDOR, Konten-Enumeration, Informationslecks und Nebenläufigkeit bewerten. Isolierte Tests nicht mit einem Audit in Produktion verwechseln.

## Éclair 2.0 — Registrierung und Wiederherstellung (v1.2, experimentell)

`references/member-email-v1.2.md` vor jeder Anfrage zur Erstellung von Konten für Kunden/Lernende oder zur Passwortwiederherstellung lesen. Das Modul `member-directory` v0.3 verwendet öffentliche POST-Routen **außerhalb des offiziellen Vertrags**; niemals eine direkte Installation auf einem unveränderten Éclair 2.0 versprechen und die E-Mail-Abläufe nicht ohne verifizierte HTTPS-URL und native Tests aktivieren. Das Erweiterungssystem von v2 jeder Änderung an der alten v0.x-Architektur vorziehen. Öffentliche Konten und Administratorkonten getrennt halten, jeden gemeinsamen Cache für Mitgliederseiten ablehnen und E-Mails als nicht zugestellt behandeln, solange keine Bestätigung vorliegt.
