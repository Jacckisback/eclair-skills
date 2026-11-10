# Validierungsplan — Tag-Manager

## Datenmodell
Container, Tags, Trigger, Einwilligung.

## Erwartete Umsetzung
Die wirklich notwendigen Tags auflisten, eine serverseitige Alternative suchen, die Blockierung durch die native Inhaltsrichtlinie dokumentieren.

## Vorzusehende Tests
1. Normalfall: Das Inventar der Tags und ihrer Alternative erstellen.
2. Ablehnungskontrolle: Ein nicht begründetes Tag wird nicht hinzugefügt.
3. Invariante: Kein Container, der das Einschleusen beliebigen Codes ohne Prüfung erlaubt.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
