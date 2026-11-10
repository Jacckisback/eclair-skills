# Validierungsplan — Stellenangebote

## Datenmodell
Angebot, Unternehmen, Status, Frist, Bewerbung und Anhänge.

## Erwartete Umsetzung
Öffentliche Filter, automatischen Ablauf, gesicherte Formulare und Aufbewahrungszyklus der Bewerbungen aufbauen.

## Vorzusehende Tests
1. Normalfall: Abgelaufene Anzeige, Spam und Export eines Bewerbers testen.
2. Ablehnungskontrolle: Ein Personalverantwortlicher kann keine Bewerbung lesen, die für ein anderes Unternehmen bestimmt ist.
3. Invariante: Lebenslauf und Anhänge werden niemals in einem über das Web zugänglichen Verzeichnis abgelegt.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
