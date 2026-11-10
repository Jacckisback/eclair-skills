# Validierungsplan — WordPress-Migration

## Datenmodell
WordPress-Export, alte IDs, Slugs, Medien, Kategorien, Autoren, Weiterleitungen und Anfragen ?p=.

## Erwartete Umsetzung
Die native WordPress-Funktion verwenden; historische URLs inventarisieren, den Import simulieren, slug/canonical vergleichen, exakte Links und Medien beibehalten, einen Rollback-Plan liefern.

## Vorzusehende Tests
1. Normalfall: URL mit abschließendem Slash, Query-Alias, Akzente, Bilder und gelöschte Seiten testen.
2. Ablehnungskontrolle: Für jede alte indexierte URL ein exaktes 200 oder eine gezielte 301-Weiterleitung erhalten.
3. Invariante: 404-Fehler und das Löschen von URLs vermeiden; niemals eine DNS-Umstellung ohne Tests und Backups.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
