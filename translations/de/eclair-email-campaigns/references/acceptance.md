# Validierungsplan — E-Mail-Kampagnen

## Datenmodell
Liste, Segment, Kampagne, Versand, Abmeldung.

## Erwartete Umsetzung
Den Versand einem spezialisierten Dienst anvertrauen, die Inhalte aus der Website vorbereiten, Segmente, Frequenz und Abmeldung festlegen.

## Vorzusehende Tests
1. Normalfall: Eine Testkampagne an eine interne Liste senden.
2. Ablehnungskontrolle: Eine abgemeldete Adresse erhält nichts mehr.
3. Invariante: Jede E-Mail enthält einen funktionierenden Abmeldelink; keine gekaufte Liste.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
