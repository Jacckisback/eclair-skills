# Validierungsplan — Automatisches Inhaltsverzeichnis

## Datenmodell
Zwischenüberschriften, Anker, Ebenen.

## Erwartete Umsetzung
Das Inhaltsverzeichnis beim serverseitigen Rendern aus den Zwischenüberschriften erzeugen, mit stabilen Ankern und ohne zwingendes JavaScript.

## Vorzusehende Tests
1. Normalfall: Das Inhaltsverzeichnis an einem Inhalt mit drei Überschriftenebenen prüfen.
2. Ablehnungskontrolle: Ein kurzer Inhalt ohne Zwischenüberschrift zeigt kein leeres Inhaltsverzeichnis an.
3. Invariante: Die erzeugten Anker sind escapt und eindeutig.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
