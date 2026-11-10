# Validierungsplan — Handlungsaufforderungen

## Datenmodell
Titel, Text, Schaltfläche, Ziel.

## Erwartete Umsetzung
Pro Seite eine Hauptaktion festlegen, sie an den richtigen Stellen wiederholen, Kontrast und eindeutige Beschriftung prüfen.

## Vorzusehende Tests
1. Normalfall: Jeder Schaltfläche auf dem Mobilgerät bis zu ihrem Ziel folgen.
2. Ablehnungskontrolle: Eine Schaltfläche ohne gültiges Ziel wird nicht veröffentlicht.
3. Invariante: Kein irreführender Link und keine offene Weiterleitung.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
