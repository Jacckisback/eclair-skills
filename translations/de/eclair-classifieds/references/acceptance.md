# Validierungsplan — Kleinanzeigen

## Datenmodell
Anzeige, Inserent, Kategorie, Status, Meldung.

## Erwartete Umsetzung
Aufgabe, Moderation, Laufzeit, Meldung und Kontaktvermittlung ohne Offenlegung der Kontaktdaten festlegen.

## Vorzusehende Tests
1. Normalfall: Aufgabe, Moderation, Ablauf und Meldung simulieren.
2. Ablehnungskontrolle: Eine abgelehnte oder abgelaufene Anzeige ist nicht mehr zugänglich.
3. Invariante: Keine Anzeige wird ohne Moderation veröffentlicht; Kontaktdaten niemals im Klartext angezeigt.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
