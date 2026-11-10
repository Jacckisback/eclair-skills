# Validierungsplan — Teilen-Vorschauen

## Datenmodell
Titel zum Teilen, Beschreibung, Bild zum Teilen.

## Erwartete Umsetzung
Die Share-Tags und das vom Kern erzeugte Bild prüfen, die Vorschau auf den wichtigsten Plattformen testen.

## Vorzusehende Tests
1. Normalfall: Die Vorschau eines Artikels und einer Seite testen.
2. Ablehnungskontrolle: Eine Seite ohne eigenes Bild behält standardmäßig eine korrekte Vorschau.
3. Invariante: Das Bild zum Teilen enthält keine personenbezogenen Daten und keinen irreführenden Text.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
