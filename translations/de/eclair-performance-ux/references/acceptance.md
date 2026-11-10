# Validierungsplan — Performance-UX

## Datenmodell
LCP, CLS, INP, Gewicht der Assets, CSS, JS, Cache und Schriften.

## Erwartete Umsetzung
Vorher/nachher mit tools/measure.php --check, Chrome Lighthouse und langsamem Netz messen, Bilder und Skripte optimieren.

## Vorzusehende Tests
1. Normalfall: Die öffentliche Website ohne Erweiterung, mit Erweiterung und auf dem Mobilgerät testen.
2. Ablehnungskontrolle: Eine behauptete Verbesserung wird von reproduzierbaren Vorher/nachher-Messungen begleitet.
3. Invariante: Den PHP-Cache-Pfad nicht verschlechtern und die CSP nicht aus Bequemlichkeit deaktivieren.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
