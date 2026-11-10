# Validierungsplan — Speisekarte

## Datenmodell
Gericht, Preis, Allergene, Kategorie, Verfügbarkeit.

## Erwartete Umsetzung
Die vom Gastronomen gelieferte Karte erfassen, Preise und Allergene anzeigen, eine lesbare HTML-Version statt nur eines PDF bereithalten.

## Vorzusehende Tests
1. Normalfall: Die veröffentlichte Karte mit dem Gastronomen auf dem Mobilgerät gegenlesen.
2. Ablehnungskontrolle: Ein Gericht ohne bestätigte Allergeninformation wird gemeldet, nicht ergänzt.
3. Invariante: Kein Preis und kein Allergen wird erfunden oder abgeleitet.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
