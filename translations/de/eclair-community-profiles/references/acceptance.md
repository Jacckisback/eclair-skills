# Validierungsplan — Community-Profile

## Datenmodell
Eindeutiges Pseudonym, Avatar, Sichtbarkeitseinstellungen, Reputation und Rollen.

## Erwartete Umsetzung
Interne ID und Pseudonym unterscheiden; Grenzen und Moderation für Avatare durchsetzen; nur freigegebene Felder offenlegen; Umbenennungen und sichere Weiterleitungen verwalten.

## Vorzusehende Tests
1. Normalfall: Kollision von Pseudonymen und Löschung des Kontos testen.
2. Ablehnungskontrolle: Ein Besucher kann aus einer Fehlermeldung oder einer Profil-API keine E-Mail-Adresse ableiten.
3. Invariante: E-Mail, Sitzung, IP, Adresse und Wiederherstellungsinformationen bleiben privat.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
