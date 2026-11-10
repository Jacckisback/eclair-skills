# Validierungsplan — Filter und Sortierung des Katalogs

## Datenmodell
Kriterium, Wert, Kombination, gefilterte Adresse.

## Erwartete Umsetzung
Auf die nativen Kategoriefilter stützen; browserseitige Filter auf öffentlichen Daten ergänzen, mit kontrollierten kanonischen Adressen.

## Vorzusehende Tests
1. Normalfall: Einen Testkatalog auf dem Mobilgerät filtern und sortieren.
2. Ablehnungskontrolle: Eine Kombination ohne Ergebnis zeigt eine Meldung an, keine leere indexierbare Seite.
3. Invariante: Die Filterkombinationen erzeugen keine unendliche Zahl indexierbarer Seiten.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
