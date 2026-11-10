# Validierungsplan — Eröffnung des leichten Shops

## Datenmodell
Produkt, Preis, Kategorie, Impressum, Verkaufsbedingungen.

## Erwartete Umsetzung
Impressum und Verkaufsbedingungen veröffentlichen, den Shop eröffnen, die ersten Produktseiten anlegen, Katalog und strukturierte Daten prüfen.

## Vorzusehende Tests
1. Normalfall: Den Shop auf einer Kopie eröffnen und Katalog und Produktseite durchgehen.
2. Ablehnungskontrolle: Der Shop öffnet nicht ohne veröffentlichte rechtliche Seiten.
3. Invariante: Keine vom Agenten erfundenen Preise, Fristen oder Verkaufsbedingungen.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
