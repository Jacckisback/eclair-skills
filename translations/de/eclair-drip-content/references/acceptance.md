# Validierungsplan — Schrittweise Freischaltung

## Datenmodell
Lektion, Freischaltregel, Datum oder Bedingung, Eingeschriebener.

## Erwartete Umsetzung
Die Regeln beschreiben (Datum, Frist nach der Einschreibung, vorherige Lektion), sie serverseitig bei jeder Anfrage anwenden.

## Vorzusehende Tests
1. Normalfall: Das Verstreichen der Zeit und den Abschluss einer Lektion simulieren.
2. Ablehnungskontrolle: Eine erratene Adresse einer gesperrten Lektion gibt deren Inhalt nicht zurück.
3. Invariante: Eine gesperrte Lektion wird niemals an den Browser gesendet, auch nicht ausgeblendet.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
