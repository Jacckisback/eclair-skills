# Validierungsplan — Umfragen und Befragungen

## Datenmodell
Frage, Auswahl, Antwort, anonymer Teilnehmer, aggregierte Ergebnisse.

## Erwartete Umsetzung
Anonymität, Begrenzung von Mehrfachabstimmungen, Anzeige der aggregierten Ergebnisse und Dauer der Umfrage festlegen.

## Vorzusehende Tests
1. Normalfall: Abstimmen, die Ergebnisse einsehen und die Umfrage schließen.
2. Ablehnungskontrolle: Eine zweite Stimme desselben Teilnehmers wird ignoriert.
3. Invariante: Keine einzelne Antwort wird veröffentlicht; nur aggregierte Ergebnisse.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
