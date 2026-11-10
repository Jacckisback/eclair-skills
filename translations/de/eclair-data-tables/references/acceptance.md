# Validierungsplan — Datentabellen

## Datenmodell
Tabelle, Kopfzeilen, Zeilen, Beschriftung.

## Erwartete Umsetzung
Den nativen Tabellen-Block verwenden, Beschriftung und Kopfzeilen ergänzen, ein kontrolliertes horizontales Scrollen vorsehen.

## Vorzusehende Tests
1. Normalfall: Die Tabelle auf dem Mobilgerät und mit dem Screenreader lesen.
2. Ablehnungskontrolle: Eine breite Tabelle verursacht kein horizontales Scrollen der gesamten Seite.
3. Invariante: Keine personenbezogenen Daten in einer öffentlichen Tabelle ohne Einwilligung.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
