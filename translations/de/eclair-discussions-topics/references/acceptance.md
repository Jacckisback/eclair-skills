# Validierungsplan — Themen und Antworten

## Datenmodell
Thema, Antwort, Version, Autor, Zeitstempel, angeheftet, geschlossen, gelöscht.

## Erwartete Umsetzung
Verschachtelung der Antworten, Paginierung, Bearbeitungsverlauf, Erwähnungen und Permalinks festlegen; Einsendungen idempotent behandeln.

## Vorzusehende Tests
1. Normalfall: Gleichzeitige Antworten, gelöschten Beitrag und geschlossenes Thema testen.
2. Ablehnungskontrolle: Ein Mitglied kann die Antwort eines anderen ohne ausdrückliches Recht weder bearbeiten noch löschen.
3. Invariante: Markdown/HTML maskieren und die Bearbeitungsberechtigung für jede Veröffentlichung prüfen.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
