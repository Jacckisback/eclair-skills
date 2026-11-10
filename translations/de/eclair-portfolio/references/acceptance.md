# Validierungsplan — Portfolio und Referenzen

## Datenmodell
Referenzprojekt, Kunde, Kontext, Ergebnis, Bilder.

## Erwartete Umsetzung
Jedes Referenzprojekt als Problem, Lösung, Ergebnis verfassen, mit leichten Bildern und Zustimmung des Kunden.

## Vorzusehende Tests
1. Normalfall: Liste und Detailansicht auf dem Mobilgerät durchgehen.
2. Ablehnungskontrolle: Ein Referenzprojekt ohne festgehaltene Zustimmung bleibt im Entwurf.
3. Invariante: Kein Kunde, keine Zahl und kein Ergebnis wird ohne Zustimmung veröffentlicht.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
