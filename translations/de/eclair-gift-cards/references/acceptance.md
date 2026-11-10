# Validierungsplan — Geschenkkarten

## Datenmodell
Karte, Code, Guthaben, Gültigkeit.

## Erwartete Umsetzung
Nicht vorhersagbare Codes erzeugen, das Guthaben serverseitig führen, den Ablauf nach dem anwendbaren Recht behandeln.

## Vorzusehende Tests
1. Normalfall: Kauf, teilweise Einlösung und Restguthaben simulieren.
2. Ablehnungskontrolle: Ein aufgebrauchter oder abgelaufener Code wird abgelehnt.
3. Invariante: Ein Code ist niemals erratbar und niemals über sein Guthaben hinaus wiederverwendbar.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
