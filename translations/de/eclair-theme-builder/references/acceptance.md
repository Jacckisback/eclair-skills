# Validierungsplan — Theme-Erstellung

## Datenmodell
theme.json, Styles, Assets, deklarierte Templates, Lizenz und Herkunft.

## Erwartete Umsetzung
Vom offiziellen Beispiel-Theme ausgehen, unterstützte Variablen und Vorlagen verwenden, erst die Preview und dann das ZIP testen, die Versionskompatibilität prüfen.

## Vorzusehende Tests
1. Normalfall: Theme-Validator, Aktivierung, Vorschau und Rollback testen.
2. Ablehnungskontrolle: Ein fehlerhaftes Template macht die Website dank des vorgesehenen Rückfalls nicht unerreichbar.
3. Invariante: Niemals SEO head und canonical neu bauen und niemals Kerndateien anfassen.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
