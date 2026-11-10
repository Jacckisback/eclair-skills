# Validierungsplan — Navigationsmenüs

## Datenmodell
Menü, Eintrag, Reihenfolge, Ziel, Position.

## Erwartete Umsetzung
Das Hauptmenü auf die wesentlichen Nutzerwege beschränken, den Rest im Fußbereich unterbringen, Tastatur und Mobilgerät testen.

## Vorzusehende Tests
1. Normalfall: Die Menüs zusammenstellen und per Tastatur und auf dem Mobilgerät durchgehen.
2. Ablehnungskontrolle: Eine zurückgezogene Seite verschwindet aus dem Menü oder wird gemeldet, niemals aus der Navigation heraus als 404 ausgeliefert.
3. Invariante: Kein Menülink zeigt auf einen Entwurf oder eine ungewollte externe Adresse.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
