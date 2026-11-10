# Validierungsplan — Produktkatalog

## Datenmodell
Produkt, SKU, Slug, Titel, Beschreibung, Anzeigepreis, Medium, Verfügbarkeit und Kategorie.

## Erwartete Umsetzung
Zuerst eine öffentliche, cachefähige GET-Seite als Prototyp bauen; ein Produktschema und seinen Index erstellen; Quelltitel und -beschreibungen beibehalten; Paginierung und canonical festlegen; die Slugs über alle Bearbeitungen hinweg erhalten.

## Vorzusehende Tests
1. Normalfall: Kategorien, leere Listen, kanonische URL, Suche und Soft-Delete testen.
2. Ablehnungskontrolle: Ein gelöschtes oder privates Produkt darf weder im Katalog noch in einem alten Cache verbleiben.
3. Invariante: Der angezeigte Preis wird bei einer künftigen Bestellung niemals als maßgebliche Quelle herangezogen.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
