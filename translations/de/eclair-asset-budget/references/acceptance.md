# Validierungsplan — Gewichtsbudget

## Datenmodell
Budget je Ressourcentyp, Messung, Abweichung.

## Erwartete Umsetzung
Budgets je Seitentyp festlegen, mit dem Werkzeug des Kerns messen, jede Ergänzung ablehnen, die sie ohne Begründung überschreitet.

## Vorzusehende Tests
1. Normalfall: Die Budgetmessung auf der Website und auf dem erzeugten Paket ausführen.
2. Ablehnungskontrolle: Ein Paket, das das Budget überschreitet, wird nicht unverändert ausgeliefert.
3. Invariante: Keine Drittanbieter-Abhängigkeit wird für eine dekorative Funktion geladen.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
