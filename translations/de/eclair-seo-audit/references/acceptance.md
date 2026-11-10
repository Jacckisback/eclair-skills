# Validierungsplan — Technisches SEO-Audit

## Datenmodell
URLs, Canonicals, Sitemap, Weiterleitungen, Titel, HTTP-Status, strukturierte Daten.

## Erwartete Umsetzung
Die erlaubten Seiten crawlen, Abweichungen festhalten, strukturelle Ursachen priorisieren, Abdeckung und Korrekturplan prüfen.

## Vorzusehende Tests
1. Normalfall: Slash, Akzente, Paginierungen, 404, Sitemap und robots testen.
2. Ablehnungskontrolle: Keine kritische URL ist nach dem Update verwaist oder in einer Kette weitergeleitet.
3. Invariante: Kein Ranking versprechen; die bestehenden URLs nicht ohne Plan für die Redirects ändern.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
