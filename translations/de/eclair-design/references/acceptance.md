# Validierungsplan — Art Direction Éclair

## Datenmodell
Positionierung, Identität, Typografie, Farben, Komponenten, Fotografien und echter Inhalt.

## Erwartete Umsetzung
Eine aus dem Geschäftsfeld abgeleitete Bildwelt definieren, Abschnitte zusammenstellen, CSS anpassen und Themes mit echtem Inhalt testen; site/themes und die vorhandenen Blöcke bevorzugen.

## Vorzusehende Tests
1. Normalfall: Kontrast, seitenübergreifende Kohärenz und mobile Versionen testen.
2. Ablehnungskontrolle: Das neue Erscheinungsbild bleibt ohne JavaScript lesbar und respektiert die vorhandenen Links.
3. Invariante: Niemals app/theme/ ändern und niemals das SEO, die CSP oder den schnellen Pfad beschädigen.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
