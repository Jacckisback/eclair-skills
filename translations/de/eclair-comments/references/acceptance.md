# Validierungsplan — Kommentare

## Datenmodell
Kommentar, Autor, Moderationsstatus, Artikel, Datum.

## Erwartete Umsetzung
Moderationswarteschlange, Spamschutzregeln, rechtliche Hinweise und Anzeige aus dem Cache festlegen; bis dahin einen externen Dienst oder eine Kontaktaufnahme vorschlagen.

## Vorzusehende Tests
1. Normalfall: Einreichen, Moderieren, Veröffentlichen und Löschen eines Kommentars simulieren.
2. Ablehnungskontrolle: Ein wartender oder abgelehnter Kommentar erscheint niemals in einer Seite aus dem Cache.
3. Invariante: Kein Kommentar wird ohne Moderation angezeigt; keine E-Mail-Adresse wird öffentlich gemacht.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
