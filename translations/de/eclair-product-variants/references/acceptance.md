# Validierungsplan — Varianten und Attribute

## Datenmodell
Übergeordnetes Produkt, Varianten mit eindeutiger SKU, Attributkombinationen, eigene Preise/Bestände, Medium und Status.

## Erwartete Umsetzung
Die maximale Anzahl der Kombinationen festlegen; die Eindeutigkeit der SKU sicherstellen; die Varianten in die GET-Ausgabe projizieren; eine beim Checkout serverseitig validierte Auswahl vorbereiten.

## Vorzusehende Tests
1. Normalfall: Fehlende, ausverkaufte und deaktivierte Varianten testen.
2. Ablehnungskontrolle: Zwei Kombinationen erzeugen dieselbe SKU => ausdrückliche Ablehnung vor der Veröffentlichung.
3. Invariante: Niemals vom Browser gesendete Preise, Gewichte oder Bestände als verlässliche Daten akzeptieren.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
