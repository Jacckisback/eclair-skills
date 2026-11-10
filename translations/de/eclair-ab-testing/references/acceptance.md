# Validierungsplan — A/B-Tests

## Datenmodell
Variante, Aufteilung, Ziel, Ergebnis.

## Erwartete Umsetzung
In aufeinanderfolgenden Zeiträumen oder über getrennte Adressen testen statt über Varianten im Cache; Hypothese, Dauer und Messung im Voraus festlegen.

## Vorzusehende Tests
1. Normalfall: Einen Test auf zwei getrennten Landingpages durchführen.
2. Ablehnungskontrolle: Ein Ergebnis ohne ausreichendes Volumen wird nicht als aussagekräftig dargestellt.
3. Invariante: Keine Variante wird besucherabhängig im gemeinsamen Cache gespeichert.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
