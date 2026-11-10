# Validierungsplan — Google Analytics

## Datenmodell
Mess-ID, Einwilligung, Ereignisse.

## Erwartete Umsetzung
Zuerst prüfen, ob eine Messung ohne Cookie genügt; andernfalls vorherige Einwilligung und Feststellung, dass die native Inhaltsrichtlinie für Erweiterungen nicht geöffnet ist.

## Vorzusehende Tests
1. Normalfall: Prüfen, dass vor der Einwilligung keine Anfrage erfolgt.
2. Ablehnungskontrolle: Nach einer Ablehnung werden keine Daten gesendet.
3. Invariante: Kein Messskript wird vor der Einwilligung oder unter Umgehung der Content-Security-Policy geladen.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
