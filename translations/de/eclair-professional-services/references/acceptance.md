# Validierungsplan — Website für freie Berufe

## Datenmodell
Leistung, Berufsträger, Richthonorare, Kontaktaufnahme.

## Erwartete Umsetzung
Tätigkeitsbereiche und tatsächliche Werdegänge präsentieren, die Kommunikationsregeln des Berufsstands einhalten, Kontakt oder Termin anbieten.

## Vorzusehende Tests
1. Normalfall: Die Inhalte vom Berufsträger gegenlesen lassen.
2. Ablehnungskontrolle: Eine nicht anerkannte Spezialisierung wird nicht als Titel angezeigt.
3. Invariante: Kein Erfolgsversprechen und keine nach dem Berufsrecht verbotene Angabe.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
