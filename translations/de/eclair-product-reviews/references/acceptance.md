# Validierungsplan — Produktbewertungen

## Datenmodell
Bewertung, Note, Autor, verifizierter Kauf, Status.

## Erwartete Umsetzung
Kaufnachweis, Moderation, Recht auf Antwort und aggregierte Anzeige festlegen; bis dahin manuell gesammelte Kundenstimmen anbieten.

## Vorzusehende Tests
1. Normalfall: Abgabe, Moderation und Veröffentlichung einer Bewertung simulieren.
2. Ablehnungskontrolle: Eine Bewertung ohne verifizierten Kauf wird nicht als verifiziert gekennzeichnet.
3. Invariante: Keine Bewertung wird ohne Moderation veröffentlicht; keine aggregierte Note ohne echte Bewertungen.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
