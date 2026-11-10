# Validierungsplan — Hero-Bereiche

## Datenmodell
Titel, Untertitel, Bild, Schaltfläche.

## Erwartete Umsetzung
Ein präzises Versprechen formulieren, ein leichtes Bild wählen, bei einer einzigen Hauptüberschrift und einer Schaltfläche bleiben.

## Vorzusehende Tests
1. Normalfall: Die Anzeige des größten Elements auf dem Mobilgerät messen.
2. Ablehnungskontrolle: Ohne Bild bleibt der Bereich lesbar und kontrastreich.
3. Invariante: Das Hauptbild hat explizite Abmessungen und verzögert die Anzeige nicht.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
