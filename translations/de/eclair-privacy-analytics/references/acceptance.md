# Validierungsplan — Datenschutzfreundliche Reichweitenmessung

## Datenmodell
Seitenaufruf, Quelle, Zeitraum, Aggregate.

## Erwartete Umsetzung
Die Serverprotokolle oder ein selbst gehostetes Tool ohne Cookies bevorzugen; ein Drittanbieter-Skript hängt von der nativen Content-Richtlinie ab.

## Vorzusehende Tests
1. Normalfall: Die gemessenen Seitenaufrufe mit einem Testdurchlauf vergleichen.
2. Ablehnungskontrolle: Die Messung setzt kein Cookie.
3. Invariante: Keine vollständige IP-Adresse und keine Besucherkennung wird gespeichert.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
