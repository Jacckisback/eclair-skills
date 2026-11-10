# Validierungsplan — Team

## Datenmodell
Person, Funktion, Foto, Kurzbiografie.

## Erwartete Umsetzung
Den nativen Team-Block mit einheitlichen Fotos und von den Personen gelieferten Texten verwenden.

## Vorzusehende Tests
1. Normalfall: Das Team auf dem Mobilgerät mit korrekten Alternativtexten anzeigen.
2. Ablehnungskontrolle: Eine entfernte Person verschwindet auch aus den Seiten im Cache.
3. Invariante: Kein Foto und keine Information wird ohne Einwilligung der Person veröffentlicht.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
