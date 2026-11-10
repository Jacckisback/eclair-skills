# Validierungsplan — Benutzerdefinierte Felder

## Datenmodell
Feld, deklarierter Typ, validierter Wert, tragender Block oder tragende Einstellung.

## Erwartete Umsetzung
Die Felder im Manifest deklarieren (vom Kern unterstützte Typen), den Kern validieren und speichern lassen, mit Escaping ausgeben.

## Vorzusehende Tests
1. Normalfall: Einen Block mit Text-, Zahlen- und Auswahlfeldern deklarieren, dann Validierung und Ausgabe prüfen.
2. Ablehnungskontrolle: Ein Wert außerhalb des Formats wird vom Kern abgelehnt und erreicht niemals die Ausgabe.
3. Invariante: Jeder angezeigte Wert läuft durch e(); kein Feld enthält ein Geheimnis.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
