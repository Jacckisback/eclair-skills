# Validierungsplan — GEO und KI-Agenten

## Datenmodell
Überprüfbarer Inhalt, Herkunft, Semantik, llms.txt, Markdown, Schema.org.

## Erwartete Umsetzung
Struktur, faktische Antworten, Quellen und Kohärenz des Markdown auditieren; KI-Robots ohne übertriebene Versprechen kontrollieren.

## Vorzusehende Tests
1. Normalfall: Markdown-Version, strukturierte Zitate und robots.txt testen.
2. Ablehnungskontrolle: Die für Robots und Menschen angezeigten Fakten bleiben konsistent und aktuell.
3. Invariante: Internen GEO-Score, Zitierfähigkeit und garantiertes Ranking nicht verwechseln.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
