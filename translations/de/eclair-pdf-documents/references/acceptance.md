# Validierungsplan — PDF-Dokumente

## Datenmodell
Dokument, Titel, Zusammenfassung, Vorstellungsseite, Datei.

## Erwartete Umsetzung
Pro Dokument eine HTML-Vorstellungsseite mit Zusammenfassung, Download-Link und barrierefreier Alternative anlegen.

## Vorzusehende Tests
1. Normalfall: Link, Dateigröße, Dokumenttitel und Vorstellungsseite prüfen.
2. Ablehnungskontrolle: Ein entferntes PDF liefert eine saubere Antwort und keinen defekten Link in den Seiten.
3. Invariante: Kein PDF mit personenbezogenen Daten wird ohne Einwilligung veröffentlicht.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
