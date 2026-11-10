# Validierungsplan — Verwandte Inhalte

## Datenmodell
Inhalt, Kategorie, gemeinsame Wörter, berechnete Linkliste.

## Erwartete Umsetzung
Die Zuordnungen bei der Veröffentlichung oder per Aufgabe berechnen, sie über einen statischen, cachefähigen Block ausgeben, auf wenige Links begrenzen.

## Vorzusehende Tests
1. Normalfall: Die vorgeschlagenen Links bei mehreren Artikeln aus verschiedenen Kategorien prüfen.
2. Ablehnungskontrolle: Ein gelöschter Artikel wird nach der Neugenerierung nicht mehr vorgeschlagen.
3. Invariante: Keine Zuordnung zeigt auf einen nicht veröffentlichten Inhalt.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
