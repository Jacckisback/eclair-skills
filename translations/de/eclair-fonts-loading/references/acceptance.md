# Validierungsplan — Schriften

## Datenmodell
Schrift, Schriftschnitte, selbst gehostete Datei, System-Fallback.

## Erwartete Umsetzung
Die Systemschriften oder die selbst gehostete Überschriftenschrift der Art Directions verwenden, die Schriftschnitte begrenzen.

## Vorzusehende Tests
1. Normalfall: Prüfen, dass es keine Drittanbieter-Anfrage und kein Springen des Textes gibt.
2. Ablehnungskontrolle: Eine nicht verfügbare Schrift hinterlässt einen lesbaren Fallback.
3. Invariante: Keine Schrift wird von einem Drittanbieter-Dienst geladen.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
