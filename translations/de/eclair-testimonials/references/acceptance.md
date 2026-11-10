# Validierungsplan — Kundenstimmen und Bewertungen

## Datenmodell
Kundenstimme, Autor, Datum, Genehmigung.

## Erwartete Umsetzung
Die echten Kundenstimmen mit schriftlicher Genehmigung einholen, sie als Zitate darstellen, die Quelle angeben.

## Vorzusehende Tests
1. Normalfall: Prüfen, dass für jede veröffentlichte Kundenstimme eine dokumentierte Genehmigung vorliegt.
2. Ablehnungskontrolle: Eine Bewertung ohne überprüfbare Quelle wird nicht veröffentlicht.
3. Invariante: Keine erfundene, veränderte oder irreführend ausgewählte Bewertung.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
