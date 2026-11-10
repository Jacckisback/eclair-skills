# Validierungsplan — Barrierefreiheit nach WCAG

## Datenmodell
Überschriftenstruktur, Tastaturnavigation, Fokus, Formulare, Medien, Kontraste.

## Erwartete Umsetzung
Ein Audit mit Tastatur und Screenreader durchführen, axe-core, Kontraste, Fehlermeldungen und reduzierte Bewegung prüfen.

## Vorzusehende Tests
1. Normalfall: Nutzerwege ohne Maus, Formularfehler und Zoom 200% testen.
2. Ablehnungskontrolle: Ein Formular bleibt ohne Farbe und über die Tastatur verständlich.
3. Invariante: Den sichtbaren Fokus nicht entfernen und keine Funktion ausschließlich von Farbe oder Geste abhängig machen.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
