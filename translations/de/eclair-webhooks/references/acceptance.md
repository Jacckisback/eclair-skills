# Validierungsplan — Eingehende und ausgehende Webhooks

## Datenmodell
Quelle, Secret, Ereignis, Signatur, Zeitstempel, eindeutige ID, Versuch, Ergebnis.

## Erwartete Umsetzung
Vertrag spezifizieren, Signatur auf den rohen Bytes prüfen, Replay-Schutz und dauerhafte Warteschlange; Retries/DLQ und privaten POST-Endpoint dokumentieren.

## Vorzusehende Tests
1. Normalfall: Doppelten Versand, Verzögerung, umgekehrte Reihenfolge und geändertes Secret testen.
2. Ablehnungskontrolle: Zwei Versuche desselben Webhooks lösen nur eine einzige fachliche Änderung aus.
3. Invariante: Niemals einen Webhook mit Secret in der URL veröffentlichen und kein unsigniertes Finanzereignis verarbeiten.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
