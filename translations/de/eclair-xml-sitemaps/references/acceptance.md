# Validierungsplan — XML-Sitemap

## Datenmodell
Sitemap-Einträge, Daten, Bilder, Sprachen.

## Erwartete Umsetzung
Die vom Kern erzeugte Sitemap kontrollieren, sie in den Tools der Suchmaschinen anmelden, die Abdeckungsfehler überwachen.

## Vorzusehende Tests
1. Normalfall: Die Sitemap validieren und mit der Anzahl der veröffentlichten Seiten vergleichen.
2. Ablehnungskontrolle: Eine Seite im Entwurf oder eine weitergeleitete Seite steht nicht darin.
3. Invariante: Die Sitemap listet nur veröffentlichte und indexierbare Seiten auf.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
