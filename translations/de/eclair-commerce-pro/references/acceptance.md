# Validierungsplan — Architektur Commerce Pro

## Datenmodell
Katalog, Warenkorb, pro Zeile eingefrorene Preise, Bestellung, Zahlung, Erstattung, Bestand, Rechnung und Statusprotokoll.

## Erwartete Umsetzung
Einen Zustandsautomaten für Bestellung/payment entwerfen, öffentliches Lesen und private Schreibvorgänge trennen, eine transaktionale Speicherung wählen, den PSP-Connector formalisieren; die von Éclair v2 nicht bereitgestellten Punkte benennen.

## Vorzusehende Tests
1. Normalfall: Kauf, Webhook-Bestätigung, Wiederholungsversuch, Erstattung, Bestand und Stornierung simulieren.
2. Ablehnungskontrolle: Dieselbe Zahlungsbenachrichtigung zweimal zugestellt => ein einziger Zustandsübergang der Bestellung.
3. Invariante: Keine Zahlung wird allein aufgrund der Browser-Weiterleitung als erfolgreich erklärt; der Server validiert ein authentifiziertes PSP-Ereignis.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
