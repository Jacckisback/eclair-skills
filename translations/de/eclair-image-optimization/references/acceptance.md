# Validierungsplan — Bildoptimierung

## Datenmodell
Quellbild, responsive Varianten, Abmessungen, Dateigröße.

## Erwartete Umsetzung
Quellen in passender Größe bereitstellen, den Kern die Varianten erzeugen lassen, die tatsächlich auf dem Mobilgerät ausgelieferte Dateigröße kontrollieren.

## Vorzusehende Tests
1. Normalfall: Ausgelieferte Dateigröße und Abmessungen auf Mobilgerät und Computer messen.
2. Ablehnungskontrolle: Kein Bild wird ohne explizite Abmessungen ausgeliefert.
3. Invariante: Sensible Metadaten (Geolokalisierung) werden nicht veröffentlicht.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
