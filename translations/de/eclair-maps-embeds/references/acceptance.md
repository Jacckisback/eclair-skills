# Validierungsplan — Karten und Anfahrtspläne

## Datenmodell
Adresse, Koordinaten, Kartenbild, Routenlink.

## Erwartete Umsetzung
Ein statisches Kartenbild mit Link zur Route bevorzugen; eine interaktive Karte eines Drittanbieters hängt von der nativen Inhaltsrichtlinie ab.

## Vorzusehende Tests
1. Normalfall: Bild, Alternativtext und Routenlink auf dem Mobilgerät prüfen.
2. Ablehnungskontrolle: Keine Anfrage an einen Kartendienst beim Laden der Seite.
3. Invariante: Keine Karte eines Drittanbieters wird vor einer Aktion des Besuchers geladen.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
