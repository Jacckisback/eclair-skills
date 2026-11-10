# Validierungsplan — Bestellungen und Zahlungen

## Datenmodell
Bestellung, Zahlungsversuch, Anbieterkennung, Webhook-Nachweis, idempotency key, Erstattung.

## Erwartete Umsetzung
Die zulässigen Übergänge im Detail festlegen; den Nachweis der Benachrichtigung und ihren Zeitstempel speichern; den Webhook dauerhaft verarbeiten; reconciliation und Teilerstattung vorsehen.

## Vorzusehende Tests
1. Normalfall: Umgekehrten, außer der Reihe eintreffenden und erneut gesendeten Webhook sowie abgelehnte Zahlung testen.
2. Ablehnungskontrolle: Ein Webhook ohne gültige Signatur ändert weder die Bestellung noch den LMS-Zugang.
3. Invariante: Niemals rohe Kreditkartendaten speichern; beim Anbieter gehosteter Checkout und geprüfte Signatur der Webhooks.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
