# Validierungsplan — Simulatoren und Rechner

## Datenmodell
Parameter, Formel, Ergebnis.

## Erwartete Umsetzung
Im Browser mit einer vom Kunden freigegebenen Formel rechnen, Annahmen und Grenzen anzeigen, anschließend die Kontaktaufnahme anbieten.

## Vorzusehende Tests
1. Normalfall: Die Ergebnisse mit einem Satz von Hand berechneter Fälle vergleichen.
2. Ablehnungskontrolle: Ein unsinniger oder negativer Wert zeigt eine Meldung an, kein falsches Ergebnis.
3. Invariante: Das Ergebnis ist unverbindlich und wird als solches ausgewiesen; keine Eingabe wird an den Server gesendet.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
