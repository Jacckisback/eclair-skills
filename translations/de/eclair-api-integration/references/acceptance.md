# Validierungsplan — API-Konnektoren

## Datenmodell
OAuth/Token, Scopes, Kontingente, Fehler, Paginierung, Version und Protokolle.

## Erwartete Umsetzung
API-Schema festlegen, Secrets isolieren, eingehende Schemata validieren, Timeouts/Circuit Breaker und Versionierung vorsehen.

## Vorzusehende Tests
1. Normalfall: Timeout, 429, 500, fehlerhaft formatierte Antwort und Widerruf testen.
2. Ablehnungskontrolle: Ein 500 des Anbieters beschädigt weder die lokalen Daten noch die öffentliche Darstellung.
3. Invariante: Kein SSRF und keine beliebigen dynamischen URLs zulassen; niemals ein Token protokollieren.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
