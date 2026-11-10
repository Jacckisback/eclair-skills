# Validierungsplan — Preistabellen

## Datenmodell
Angebot, Preis, Zeitraum, Merkmale, Schaltfläche.

## Erwartete Umsetzung
Die Angebote als vergleichbare Karten zusammenstellen, Brutto- oder Nettopreis unmissverständlich anzeigen und jede Schaltfläche mit der richtigen Aktion verknüpfen.

## Vorzusehende Tests
1. Normalfall: Drei Angebote auf dem Mobilgerät vergleichen und jeden Link prüfen.
2. Ablehnungskontrolle: Ein Angebot ohne freigegebenen Preis wird nicht angezeigt.
3. Invariante: Keine erfundenen Preise, Rabatte oder rechtlichen Hinweise.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
