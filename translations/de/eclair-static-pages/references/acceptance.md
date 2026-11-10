# Validierungsplan — Seiten der Website

## Datenmodell
Seite, Adresse, Blöcke, übergeordnete Seite, Status, Menüeintrag.

## Erwartete Umsetzung
Die benötigten Seiten auflisten, die Adressen vor dem Schreiben festlegen, jede Seite aus Blöcken aufbauen und die Seiten untereinander verlinken.

## Vorzusehende Tests
1. Normalfall: Die vollständige Seitenstruktur anlegen und jede Adresse, das Menü und die Brotkrumennavigation kontrollieren.
2. Ablehnungskontrolle: Eine umbenannte Seite antwortet mit einer einzigen 301-Weiterleitung, niemals mit einem 404-Fehler.
3. Invariante: Niemals die Adresse einer veröffentlichten Seite ohne geprüfte Weiterleitung ändern.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
