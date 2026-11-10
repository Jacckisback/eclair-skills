# Validierungsplan — Strukturierte Daten

## Datenmodell
WebPage, Article, Product, passende FAQ, Organization, BreadcrumbList.

## Erwartete Umsetzung
Das native JSON-LD untersuchen, bevor ein Typ hinzugefügt wird; Duplikate vermeiden; jedes Feld an den sichtbaren Daten und den Vorgaben der Suchmaschinen ausrichten.

## Vorzusehende Tests
1. Normalfall: Gültiges JSON, canonical, Kennungen und angezeigten Inhalt testen.
2. Ablehnungskontrolle: Kein Preis/keine Bewertung/kein product, der erfunden ist oder auf der Seite fehlt, steht im JSON-LD.
3. Invariante: Éclair v2 stellt Erweiterungen noch nicht alle JSON-LD-Beiträge bereit; lieber einen RFC vorschlagen als eine undurchsichtige Injektion.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
