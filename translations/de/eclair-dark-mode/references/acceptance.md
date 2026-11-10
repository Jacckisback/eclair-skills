# Validierungsplan — Dunkler Modus

## Datenmodell
Helles und dunkles Farbschema, Präferenz des Besuchers.

## Erwartete Umsetzung
Die Farbvariablen des Themes für prefers-color-scheme definieren, Kontraste, Bilder und Logos prüfen.

## Vorzusehende Tests
1. Normalfall: Die Kontraste beider Modi auf den Seitentypen kontrollieren.
2. Ablehnungskontrolle: Ein dunkles Logo wird im dunklen Modus nicht unsichtbar.
3. Invariante: Kein Cookie ist nötig, um die Systempräferenz zu beachten.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
