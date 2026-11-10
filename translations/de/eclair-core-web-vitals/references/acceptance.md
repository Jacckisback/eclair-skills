# Validierungsplan — Core Web Vitals

## Datenmodell
Anzeige des größten Elements, Stabilität, Reaktionsfähigkeit, je Template.

## Erwartete Umsetzung
Im Labor und, wenn vorhanden, auf realen Daten messen, die Hauptursache je Template beheben, erneut messen.

## Vorzusehende Tests
1. Normalfall: Drei Templates auf dem Mobilgerät vor und nach der Korrektur messen.
2. Ablehnungskontrolle: Eine nicht gemessene Verbesserung wird nicht als erreicht gemeldet.
3. Invariante: Kein Score wird versprochen; nur die gemessenen Ergebnisse werden berichtet.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
