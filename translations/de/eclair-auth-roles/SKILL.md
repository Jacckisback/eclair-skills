---
name: eclair-auth-roles
description: Use when reviewing Éclair v2 admin rights or designing member, student, customer and moderator authentication beyond the admin-only built-in roles.
---

# Éclair Auth & Roles — Admin und Mitglieder unterscheiden

## Realität in v2
`Eclair\Auth` und `Users` kontrollieren **die Administration** mit ihren Rechten (`content`, `settings`, `security` usw.). Sie sind kein Verzeichnis für Kunden, Lernende oder Mitglieder und dürfen nicht zu Rollen `customer/student` zweckentfremdet werden.

## Vorgehen
1. `Users`, `Auth`, `Admin`, `Security`, `Session`, `RateLimit` und das von jeder Admin-Route `eclair-extension/1` verlangte Recht einsehen.
2. Für eine Administrationsfunktion `routes.admin[]` mit exaktem `right` deklarieren und sich auf die CSRF-Prüfung des Kerns stützen. Den Zugriff für jede bestehende Rolle prüfen.
3. Für einen öffentlichen Bereich für Kunden/Lernende: ein RFC für einen Identitätsanbieter oder eine dedizierte, auditierte Serverkomponente mit geeignetem Speicher erstellen; sensible Routen **nicht** über öffentliches GET exponieren.
4. Die unabhängige Mitgliedersitzung, die Cookies `Secure/HttpOnly/SameSite`, die stufenweisen Authentifizierungen, Rate Limiting, Wiederherstellung und E-Mail-Verifizierung festlegen.
5. Berechtigungen: das Subjekt systematisch über eine verifizierte Serversitzung identifizieren, dann bei jeder Anfrage das Objekt und den Geltungsbereich kontrollieren (IDOR/BOLA).
6. Testen: keine vom Admin geerbten Privilegien, Rollenwechsel, Widerruf, Reset, Race Conditions bei Sitzungen, kontoübergreifender Zugriff, CSRF und Ablehnung als Standard.

## Nativer Demonstrator v1.0
Die Erweiterung `examples/extensions/member-directory/` liefert ein Beispiel **nur für Admin** für Éclair 2.0:
- `routes.admin`: GET + POST (`users`) mit verstärkten Kontrollen in den Handlern; `routes.public`: leeres Array.
- `MemberAccounts` und `MemberSessions` bleiben unabhängig von `Eclair\Users/Auth/Session`; Konto `pending` bei der Bereitstellung zwingend.
- Die Daten liegen ausschließlich unter `data/ext/member-directory/` über `Store`. Niemals in `data/users.php`.
- `MemberPermissions::allows` nimmt ein verifiziertes Sitzungstoken entgegen, keine vom Aufrufer gelieferte Identität.
- Weder öffentliche Registrierung noch E-Mail-Versand, noch Passwortwiederherstellung, noch echte Verwaltung von HTTP-Sitzungen ist aktiviert.
- Die öffentliche POST-API erfordert ein RFC/einen neuen Vertrag des Kerns und eine durchgängige Validierung vor dem Deployment.
`references/member-directory-v1.md` lesen, bevor ein LMS, ein Forum oder ein Shop gebaut wird.

## Liefergegenstände
Matrix der Berechtigungen und Ressourcen, Bedrohungsmodell, Identitätsplan, Testsätze und Angabe „native / RFC erforderlich“.

## Éclair 2.0 — Prototyp v1.1 (experimentell)
Der Prototyp v1.1 besitzt öffentliche Handler: GET für das Formular + POST für Anmeldung/Abmeldung + GET für den privaten Bereich. Sie sind erst nach der genehmigten Aufnahme des POST-Vertrags gültig. Mitgliedersitzungen getrennt von denen der Admins, opakes Token, Double-Submit-CSRF und Sitzungs-CSRF bei der Abmeldung; keine Rolle admin/editor wird vergeben.

## Éclair 2.0 — Registrierung und Wiederherstellung (v1.2, experimentell)

`references/member-email-v1.2.md` vor jeder Anfrage zur Erstellung von Konten für Kunden/Lernende oder zur Passwortwiederherstellung lesen. Das Modul `member-directory` v0.3 verwendet öffentliche POST-Routen **außerhalb des offiziellen Vertrags**; niemals eine direkte Installation auf einem unveränderten Éclair 2.0 versprechen und die E-Mail-Abläufe nicht ohne verifizierte HTTPS-URL und native Tests aktivieren. Das Erweiterungssystem von v2 jeder Änderung an der alten v0.x-Architektur vorziehen. Öffentliche Konten und Administratorkonten getrennt halten, jeden gemeinsamen Cache für Mitgliederseiten ablehnen und E-Mails als nicht zugestellt behandeln, solange keine Bestätigung vorliegt.
