# Validierungsplan — Sprachen von rechts nach links

## Datenmodell
Textrichtung, logische CSS-Eigenschaften, richtungsabhängige Icons.

## Erwartete Umsetzung
Im Website-Theme die logischen CSS-Eigenschaften verwenden, jede Vorlage mit dir=rtl testen.

## Vorzusehende Tests
1. Normalfall: Die Seitentypen von rechts nach links ohne Überlauf anzeigen.
2. Ablehnungskontrolle: Eine Mischung von Sprachen bricht die Lesereihenfolge nicht.
3. Invariante: Kein Benutzertext wird ohne Escaping eingefügt, Richtungszeichen eingeschlossen.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
