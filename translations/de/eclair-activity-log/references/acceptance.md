# Validierungsplan — Aktivitätsprotokoll

## Datenmodell
Ereignis, Konto, Datum, Aktion.

## Erwartete Umsetzung
Das Protokoll der Seite Sicherheit einsehen, Anmeldungen und sensible Änderungen ausfindig machen, eine Kontrollroutine festlegen.

## Vorzusehende Tests
1. Normalfall: Eine sensible Aktion auslösen und sie im Protokoll wiederfinden.
2. Ablehnungskontrolle: Ein Konto ohne das Recht Sicherheit hat keinen Zugriff auf das Protokoll.
3. Invariante: Das Protokoll ist nur für die Konten mit dem Recht Sicherheit lesbar.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
