# Validierungsplan — Mehrsprachiges SEO

## Datenmodell
Sprache, URL der Übersetzung, wechselseitiges hreflang, Titel und Sitemap.

## Erwartete Umsetzung
Veröffentlichte Sprachen inventarisieren, das Mapping der Übersetzungen festlegen, canonical pro Sprache, hreflang/x-default und das Fehlen aufdringlicher Weiterleitungen testen.

## Vorzusehende Tests
1. Normalfall: Paare FR/ES/EN, fehlende Seiten und Sprachwechsel testen.
2. Ablehnungskontrolle: Jeder hreflang-Link zeigt auf eine indexierbare und wechselseitig verknüpfte URL mit 200.
3. Invariante: Keine ungeprüfte maschinelle Übersetzung als endgültige Seite verwenden.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
