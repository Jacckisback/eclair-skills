# Validierungsplan — Inhalte für Anwendungen und KI

## Datenmodell
Markdown-Version, llms.txt, Feeds, Sitemap.

## Erwartete Umsetzung
Auf die nativen maschinenlesbaren Ausgaben stützen, ihr Format und ihre Aktualität für die Client-Anwendung dokumentieren.

## Vorzusehende Tests
1. Normalfall: Eine Seite in HTML und in Markdown lesen und vergleichen.
2. Ablehnungskontrolle: Ein Entwurf hat keine zugängliche Markdown-Version.
3. Invariante: Kein privater Inhalt wird durch diese Ausgaben offengelegt.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
