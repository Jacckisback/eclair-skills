# Validierungsplan — Aktionen und Gutscheine

## Datenmodell
Code, Budget, Daten, Kontingent, Warenkorbbedingungen, Verwendungen und Ausschlüsse.

## Erwartete Umsetzung
Berechnungsreihenfolge und Rundung festlegen; den Gutschein vor der Bestellung prüfen; die Verwendungen atomar zählen; Stornierung und Rückgabe nachverfolgen.

## Vorzusehende Tests
1. Normalfall: Abgelaufene und aufgebrauchte Gutscheine, Schwellenwert und Ausschlüsse testen.
2. Ablehnungskontrolle: Zwei gleichzeitige Bestellungen können nicht den letzten einmaligen Gutschein verbrauchen.
3. Invariante: Die Entscheidung über die Berechtigung stammt aus den Serverdaten und nicht aus dem im HTML eingegebenen Rabatt.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
