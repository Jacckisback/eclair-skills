# Validierungsplan — Spenden und Vereine

## Datenmodell
Anliegen, Projekt, Betrag, Spendenlink, Quittung.

## Erwartete Umsetzung
Auftrag und Mittelverwendung präsentieren, die Spendenschaltflächen mit Links des Dienstleisters verknüpfen, die Verwaltung der Quittungen dem Dienstleister oder dem Verein überlassen.

## Vorzusehende Tests
1. Normalfall: Eine Spende im Testmodus tätigen und den gesamten Ablauf verfolgen.
2. Ablehnungskontrolle: Ein in der Seite geänderter Betrag ändert den eingezogenen Betrag nicht.
3. Invariante: Kein Versprechen eines Steuervorteils ohne Bestätigung des Vereins.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
