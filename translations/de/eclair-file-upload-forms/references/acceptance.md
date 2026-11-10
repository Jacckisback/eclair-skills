# Validierungsplan — Formulare mit Dateianhängen

## Datenmodell
Hochgeladene Datei, Typ, Größe, Eigentümer, Aufbewahrungsdauer.

## Erwartete Umsetzung
Akzeptierte Typen und Größen, Speicherung außerhalb des öffentlichen Wurzelverzeichnisses, Prüfung und automatische Löschung festlegen.

## Vorzusehende Tests
1. Normalfall: Eine gültige Datei hochladen und sie in der Administration wiederfinden.
2. Ablehnungskontrolle: Eine zu große, getarnte oder ausführbare Datei wird abgelehnt.
3. Invariante: Keine hochgeladene Datei ist ausführbar oder wird direkt an die Öffentlichkeit ausgeliefert.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
