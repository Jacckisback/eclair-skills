# Validierungsplan — Unterkünfte und Zimmer

## Datenmodell
Zimmer, Kapazität, Ausstattung, Richtpreise, Buchungslink.

## Erwartete Umsetzung
Jede Unterkunft als Einzelseite präsentieren, auf das vorhandene Buchungssystem oder die Anfrage per Formular verweisen.

## Vorzusehende Tests
1. Normalfall: Einzelseiten und Buchungslink auf dem Mobilgerät durchgehen.
2. Ablehnungskontrolle: Ein zurückgezogenes Zimmer wird nicht mehr angeboten.
3. Invariante: Keine Verfügbarkeit und kein Preis wird als garantiert angezeigt, wenn sie nicht aus dem Buchungssystem stammen.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
