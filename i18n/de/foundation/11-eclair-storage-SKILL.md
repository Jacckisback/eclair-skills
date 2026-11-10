---
name: eclair-storage
description: Use when choosing Éclair CMS v2 extension persistence, migrations, backups or SQL requirements for commerce, forums or course progress.
---

# Éclair Storage — die richtige Persistenz wählen

## Speicherentscheidung
1. Für Inhalte und Einstellungen von Éclair `Eclair\Store` und das über `$ctx['data']` erhaltene Präfix `data/ext/<id>/` verwenden.
2. `Store::locked`, atomare Schreibvorgänge und die tatsächlich verarbeiteten Datenmengen prüfen; keine transaktionale Garantie über mehrere Dateien erfinden.
3. Für Bestellungen/Zahlungen/Lagerbestände und nebenläufigen LMS-Fortschritt: SQLite oder MySQL **als optionale Abhängigkeit des Moduls** spezifizieren, mit Migrationen, Constraints, Transaktionen, Backup und Wiederanlauf. Der native Vertrag v2 stellt kein generisches PDO für Erweiterungen bereit.
4. Personenbezogene Daten, Aufbewahrung, Löschung und Export deklarieren; weder Schlüssel noch Token in den Sicherungen aufbewahren.
5. Native Migrationen einer Erweiterung über das Manifest `migrations[]` und die Methode `migrate`: additiv, versioniert, idempotent. Eine Migration des SQL-Schemas braucht einen eigenen Plan und darf nicht auf einer GET-Seite ausgelöst werden.
6. Konsistente Sicherung, Kaltwiederherstellung und Rollback-Test vorsehen. Ist SQL auf einem Shared Hosting nicht verfügbar, die Funktionalität als nicht verfügbar ausweisen, statt auf eine unzuverlässige Persistenz zurückzufallen.
7. Kollisionen, Neustarts, Nebenläufigkeit, Duplikate, Korruption, chmod/Symlink, Backup und Abgleich testen.

## Regeln
Der native Speicher ohne Datenbank muss für eine einfache Website möglich bleiben. Die SQL-Prototypen v0.5/v0.8 werden von v2 weder installiert noch erkannt. Für externe Effekte kein „genau einmal“ versprechen.

## Liefergegenstände
Schema, Matrix der Invarianten, Protokoll für Migration/Restore, Hosting-Anforderungen, Transaktions- und Integritätstests.

## V1.0 — Muster für leichtgewichtige Konten
Der Prototyp `member-directory` hält `data/ext/<id>/`, atomare Schreibvorgänge und eine globale Sperre ein. Die Speicherung in mehreren Dateien **ist keine SQL-Transaktion**. Das Kontingent von 1 000 Konten ist eine Laborgrenze: Jedes kommerzielle Projekt mit vielen Mitgliedern muss zuerst über den transaktionalen SQL-Vertrag verfügen.

## Éclair 2.0 — Prototyp v1.1 (experimentell)
Der Speicher des Demonstrators nutzt weiterhin die geschützten Dateien von `Store` und eine globale Sperre. Er ist auf 1000 Konten begrenzt; kein Versprechen von Atomarität über mehrere Dateien, von Zugriff in großem Maßstab oder von transaktionaler Ausfallsicherheit. Ein SQL-Backend ist Voraussetzung vor jedem geschäftlichen Einsatz.

## Éclair 2.0 — Registrierung und Wiederherstellung (v1.2, experimentell)

`references/member-email-v1.2.md` vor jeder Anfrage zur Erstellung von Konten für Kunden/Lernende oder zur Passwortwiederherstellung lesen. Das Modul `member-directory` v0.3 verwendet öffentliche POST-Routen **außerhalb des offiziellen Vertrags**; niemals eine direkte Installation auf einem unveränderten Éclair 2.0 versprechen und die E-Mail-Abläufe nicht ohne verifizierte HTTPS-URL und native Tests aktivieren. Das Erweiterungssystem von v2 jeder Änderung an der alten v0.x-Architektur vorziehen. Öffentliche Konten und Administratorkonten getrennt halten, jeden gemeinsamen Cache für Mitgliederseiten ablehnen und E-Mails als nicht zugestellt behandeln, solange keine Bestätigung vorliegt.
