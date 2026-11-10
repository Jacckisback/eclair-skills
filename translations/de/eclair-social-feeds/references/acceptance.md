# Validierungsplan — Social-Media-Feeds

## Datenmodell
Beitrag, Bild, Link, Abrufdatum.

## Erwartete Umsetzung
Die Beiträge per geplanter Aufgabe serverseitig abrufen, wenn das Netzwerk es erlaubt, sie als statisches HTML ausgeben; andernfalls einfache Links zu den Profilen.

## Vorzusehende Tests
1. Normalfall: Die statische Ausgabe und die Aktualisierung per Aufgabe prüfen.
2. Ablehnungskontrolle: Ist das Netzwerk nicht erreichbar, bleibt die letzte gültige Version angezeigt.
3. Invariante: Kein Drittanbieter-Widget wird im Browser der Besucher geladen.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
