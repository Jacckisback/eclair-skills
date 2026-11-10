# Validierungsplan — Warenkorb und Bestellprozess

## Datenmodell
Temporärer Warenkorb, Mitglieder- oder Gastsitzung, Zeilen, Aktionen, Gebühren, Steuern, Bestellstatus.

## Erwartete Umsetzung
Anzeige und Zustandsänderung trennen; jede Zeile auf dem Server erneut validieren; die Beträge in ganzen Währungseinheiten berechnen; den Bestand zum richtigen Zeitpunkt transaktional reservieren.

## Vorzusehende Tests
1. Normalfall: Gleichzeitige Änderung des Warenkorbs, Ablauf und Preisänderung testen.
2. Ablehnungskontrolle: Doppeltes oder gleichzeitiges Absenden erzeugt keine zwei zahlbaren Bestellungen für denselben Schlüssel.
3. Invariante: Kein öffentlicher Schreibvorgang vor qualifizierter POST-Route, CSRF, Kontingenten und geprüften Rechten.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
