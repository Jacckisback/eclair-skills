---
name: eclair-test-suite
description: Use when creating CI, regression, security and performance tests for Éclair CMS 2.0 themes, native extensions and advanced module integrations.
---

# Éclair Test Suite — ein Nachweis vor der Veröffentlichung

## Prüfreihenfolge
1. Den Commit und `ECLAIR_VERSION` erfassen; den offiziellen Vertrag v2 verlangen. Ohne vollständigen Checkout die Aussage auf die tatsächlich ausführbaren Tests beschränken.
2. `php -l` für jede erzeugte PHP-Datei, dann `php tools/validate.php site/extensions/<id> --json` mit dem passenden Kern.
3. `php tests/run.php --unit`, dann `php tests/run.php` (HTTP, Auth, Routen, Cache, Sicherungen, Erweiterungen, Themes, WordPress-Migration).
4. `php tools/measure.php --check`; den warmen Cache und das Speicher-/Zeitbudget mit dem unveränderten Kern vergleichen.
5. Inaktive Installation, Aktivierung, idempotente Migration, Update, Routenkonflikt, Deaktivierung, Aufbewahrung der Daten, Entfernen des Codes und gegebenenfalls manuelle Bereinigung testen.
6. Bei Mitgliederkonten/SQL: echte PHP/PDO-Tests verlangen, mit mehreren Prozessen, Autorisierungen pro Objekt, signierten Webhooks und Wiederherstellung aus einer Sicherung. `pdo_sqlite` fehlt = Test blockiert, nicht bestanden.
7. Empfohlene CI: Matrix PHP 8.1 bis 8.5, offizielle `tests.yml`, gebautes Archiv und Server Apache/Nginx; funktionsspezifische Jobs hinzufügen.
8. Eine Tabelle der Tests ausgeführt / fehlgeschlagen / blockiert erstellen. Niemals aus einer isolierten Fixture heraus „produktionskompatibel“ melden.

## Liefergegenstände
Skripte und Fixtures, Ausführungsbericht, Abdeckung der adversen Fälle, Budgets und Rollback-Strategie.

## V1.0 — Zusätzliche Prüfungen
`php tests/member-directory.php`, `python3 -m unittest discover -s tests -v` und `python3 scripts/verify_sample.py` ausführen. Auf einem vollständigen Checkout von Éclair 2.0 **zwingend** `php tools/validate.php examples/extensions/member-directory --json` ausführen, dann die PHP/HTTP-Tests des vollständigen CMS und das Budget `tools/measure.php --check`, bevor irgendein Merge vorgeschlagen wird.

## Éclair 2.0 — Prototyp v1.1 (experimentell)
`php tests/member-directory.php` + `php tests/member-public.php` sowie die Python-Tests ausführen. Auf einem echten Klon von Éclair 2.0.0 den Patch auf einen sauberen Feature-Branch anwenden, `php tools/validate.php`, `php tests/run.php`, `php tools/measure.php --check` sowie HTTP/TLS-Tests durchführen. Kein Merge ohne diese Kriterien.

## Éclair 2.0 — Registrierung und Wiederherstellung (v1.2, experimentell)

`references/member-email-v1.2.md` vor jeder Anfrage zur Erstellung von Konten für Kunden/Lernende oder zur Passwortwiederherstellung lesen. Das Modul `member-directory` v0.3 verwendet öffentliche POST-Routen **außerhalb des offiziellen Vertrags**; niemals eine direkte Installation auf einem unveränderten Éclair 2.0 versprechen und die E-Mail-Abläufe nicht ohne verifizierte HTTPS-URL und native Tests aktivieren. Das Erweiterungssystem von v2 jeder Änderung an der alten v0.x-Architektur vorziehen. Öffentliche Konten und Administratorkonten getrennt halten, jeden gemeinsamen Cache für Mitgliederseiten ablehnen und E-Mails als nicht zugestellt behandeln, solange keine Bestätigung vorliegt.
