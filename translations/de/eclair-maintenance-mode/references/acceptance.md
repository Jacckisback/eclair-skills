# Validierungsplan — Wartungsmodus

## Datenmodell
Wartungszustand, Meldung, voraussichtliche Dauer, Zugang des Teams.

## Erwartete Umsetzung
Auf Serverebene eine statische Seite mit dem richtigen temporären HTTP-Status ausliefern, den Zugang zur Administration erhalten, die Wiederinbetriebnahme einplanen.

## Vorzusehende Tests
1. Normalfall: Aktivieren, Status 503 und Retry-Header prüfen, deaktivieren.
2. Ablehnungskontrolle: Die Bots erhalten die Wartungsseite niemals mit einem Status 200.
3. Invariante: Die Wartungsseite verrät weder Version noch Serverpfad.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
