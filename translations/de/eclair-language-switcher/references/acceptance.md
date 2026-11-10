# Validierungsplan — Sprachumschalter

## Datenmodell
Aktuelle Sprache, verfügbare Versionen, Beschriftungen.

## Erwartete Umsetzung
Die Sprachen mit ihrem Namen in der jeweils eigenen Sprache auflisten, auf die entsprechende Version verweisen, ohne erzwungene automatische Weiterleitung.

## Vorzusehende Tests
1. Normalfall: Von einer tief liegenden Seite aus die Sprache wechseln und auf ihrer Entsprechung landen.
2. Ablehnungskontrolle: Ohne Entsprechung führt der Link zur Startseite der Sprache, nicht zu einem Fehler.
3. Invariante: Keine Weiterleitung anhand der IP-Adresse; die Wahl des Besuchers wird respektiert.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
