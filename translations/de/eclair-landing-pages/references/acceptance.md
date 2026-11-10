# Validierungsplan — Landingpages

## Datenmodell
Versprechen, Belege, Angebot, Handlungsaufforderung.

## Erwartete Umsetzung
Eine Seite für eine einzige Absicht schreiben, sie aus nativen Blöcken aufbauen, die Aktion mit einem Formular oder einem Zahlungslink verknüpfen.

## Vorzusehende Tests
1. Normalfall: Die Seite auf dem Mobilgerät bis zur Aktion durchgehen.
2. Ablehnungskontrolle: Ein nicht vom Kunden gelieferter Beleg erscheint nicht.
3. Invariante: Keine erfundenen Kundenstimmen, Zahlen oder Garantien.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
