# Validierungsplan — Pop-ups und Opt-in-Einblendungen

## Datenmodell
Nachricht, Auslöser, Häufigkeit, Aktion.

## Erwartete Umsetzung
Eine Einblendung innerhalb der Seite bevorzugen; andernfalls natives dialog, ausgelöst durch eine Aktion des Besuchers, per Tastatur schließbar, niemals bei der Ankunft.

## Vorzusehende Tests
1. Normalfall: Per Tastatur und auf dem Mobilgerät öffnen und schließen.
2. Ablehnungskontrolle: Die abgelehnte Einblendung erscheint während des Besuchs nicht erneut.
3. Invariante: Kein Fenster blockiert den Inhalt oder fängt den Fokus ein.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
