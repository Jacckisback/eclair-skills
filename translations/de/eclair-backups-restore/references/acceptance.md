# Validierungsplan — Sicherungen und Wiederherstellung

## Datenmodell
Sicherungsarchiv, Datum, Ziel, Wiederherstellungstest.

## Erwartete Umsetzung
Die herunterladbare Sicherung oder die Sicherung in den vom Kern vorgesehenen Remote-Speicher aktivieren, die Häufigkeit festlegen, zur Überprüfung auf einer Kopie wiederherstellen.

## Vorzusehende Tests
1. Normalfall: Die letzte Sicherung auf einer Testinstallation wiederherstellen und vergleichen.
2. Ablehnungskontrolle: Ein verändertes oder präpariertes Archiv wird bei der Wiederherstellung abgelehnt.
3. Invariante: Eine Sicherung enthält personenbezogene Daten: Sie wird verschlüsselt oder an einem sicheren Ort gespeichert, niemals in einem öffentlichen Ordner.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
