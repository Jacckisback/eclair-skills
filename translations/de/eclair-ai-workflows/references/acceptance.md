# Validierungsplan — KI-Workflows

## Datenmodell
Entwurf, Vorschlag, Freigabe, Modell, Kosten, Quelle und Audit.

## Erwartete Umsetzung
MCP-Fähigkeiten des Kerns nutzen, den Menschen in der Schleife halten, Zugriff und Budget begrenzen; Qualität und Halluzinationen bewerten.

## Vorzusehende Tests
1. Normalfall: Prompt Injection, Kontextwechsel und Rollback testen.
2. Ablehnungskontrolle: Eine feindselige Anweisung in einem importierten Artikel wird nicht zu einem ausgeführten Befehl.
3. Invariante: Keine KI veröffentlicht, deployt, löscht oder ändert PHP ohne Kontrolle direkt per MCP.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
