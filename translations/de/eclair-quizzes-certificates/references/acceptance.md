# Validierungsplan — Quiz und Bescheinigungen

## Datenmodell
Frage, Auswahl, Korrektur, Versuch, Punktzahl, Frist, Bescheinigung und Verifizierung.

## Erwartete Umsetzung
Fragenpool versionieren; serverseitig bewerten; Versuche und Zeit festlegen; signierte/verifizierbare Bescheinigung ohne öffentliche PII erzeugen.

## Vorzusehende Tests
1. Normalfall: Betrug, Sitzungsende, Validierung des Zertifikats testen.
2. Ablehnungskontrolle: Das zweimalige Einreichen eines Versuchs darf keine zwei Zertifikate erzeugen.
3. Invariante: Niemals Lösung oder richtige Antwort im HTML einer aktiven Prüfung senden.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
