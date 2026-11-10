# Validierungsplan — Live-Unterricht

## Datenmodell
Sitzung, Datum, Zeitzone, Zugangslink, Angemeldete.

## Erwartete Umsetzung
Den Sitzungskalender per GET veröffentlichen, den Zugangslink über den Videokonferenzdienst oder per E-Mail senden, nicht auf einer öffentlichen Seite.

## Vorzusehende Tests
1. Normalfall: Die Anzeige der Termine in zwei Zeitzonen prüfen.
2. Ablehnungskontrolle: Eine vergangene Sitzung wird nicht mehr zur Anmeldung angeboten.
3. Invariante: Der Link einer kostenpflichtigen oder privaten Sitzung wird niemals veröffentlicht.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
