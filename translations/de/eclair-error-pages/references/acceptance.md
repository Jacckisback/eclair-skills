# Validierungsplan — Fehlerseiten

## Datenmodell
Fehlerseite, nützliche Links, Protokoll der nicht gefundenen Adressen.

## Erwartete Umsetzung
Im Website-Theme eine nützliche 404-Seite gestalten, Startseite und Schlüsselseiten anbieten, häufige 404 per Weiterleitung behandeln.

## Vorzusehende Tests
1. Normalfall: Eine nicht existierende Adresse aufrufen und Status 404 sowie Inhalt prüfen.
2. Ablehnungskontrolle: Eine nicht gefundene Seite antwortet niemals mit einem Status 200.
3. Invariante: Die Fehlerseite zeigt keinerlei technischen Trace an.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
