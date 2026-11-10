# Validierungsplan — Blogartikel

## Datenmodell
Artikel, Auszug, Hauptbild, Kategorie, Autor, Datum, Status Entwurf oder veröffentlicht.

## Erwartete Umsetzung
Die Artikel über die Administration oder den MCP-Connector als Entwurf anlegen, Titel, Auszug, Bild und Kategorie prüfen, dann eine Person veröffentlichen lassen.

## Vorzusehende Tests
1. Normalfall: Einen vollständigen Entwurf anlegen, ihn veröffentlichen lassen, dann Darstellung, RSS-Feed und Sitemap prüfen.
2. Ablehnungskontrolle: Ein Entwurf erscheint weder auf der öffentlichen Website noch in der Sitemap noch im Feed.
3. Invariante: Niemals anstelle der berechtigten Person einen Inhalt veröffentlichen oder löschen.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
