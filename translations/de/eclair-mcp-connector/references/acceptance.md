# Validierungsplan — MCP-Konnektor

## Datenmodell
Autorisierter Client, Token, verfügbare Werkzeuge, erstellte Entwürfe.

## Erwartete Umsetzung
Den Konnektor vom Eigentümer aktivieren lassen, den Client autorisieren, mit Entwürfen und Vorschlägen arbeiten, den Zugriff kappen können.

## Vorzusehende Tests
1. Normalfall: Über den Konnektor einen Entwurf erstellen und dann den Zugriff widerrufen.
2. Ablehnungskontrolle: Nach dem Widerruf wird jede Anfrage des Clients abgelehnt.
3. Invariante: Der Konnektor veröffentlicht nicht und löscht nicht; der Zugriff ist jederzeit widerrufbar.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
