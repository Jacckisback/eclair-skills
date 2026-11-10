# Validierungsplan — Wunschlisten

## Datenmodell
Liste, Produkt, Eigentümer.

## Erwartete Umsetzung
Mit einer Speicherung im Browser ohne Konto beginnen; die Version mit Konto für später konzipieren.

## Vorzusehende Tests
1. Normalfall: Favoriten hinzufügen, entfernen und wiederfinden.
2. Ablehnungskontrolle: Ein gelöschtes Produkt verschwindet sauber aus den Listen.
3. Invariante: Keine Liste wird ohne Zutun des Eigentümers geteilt oder für Dritte sichtbar.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
