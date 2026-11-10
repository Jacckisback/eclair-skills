# Validierungsplan — Umsatzsteuer und Rechnungsstellung

## Datenmodell
Verkaufs- und Lieferland, steuerlicher Standort, geltender Satz, Rechnung, Gutschrift, Nummernfolge.

## Erwartete Umsetzung
Rechtsordnungen und Kundentypen auflisten; aktuelle Regeln und Steuerberatung heranziehen; Bemessungsgrundlage/Satz zum Zeitpunkt der Bestellung einfrieren; Exporte von Rechnungen und Gutschriften vorbereiten.

## Vorzusehende Tests
1. Normalfall: Inlandsverkauf, grenzüberschreitenden Verkauf, Erstattung und Satzänderung testen.
2. Ablehnungskontrolle: Eine ausgestellte und dann stornierte Rechnung darf nicht stillschweigend gelöscht oder neu nummeriert werden.
3. Invariante: Niemals einen universellen Umsatzsteuersatz anwenden oder vorgeben, steuerliche Konformität ohne lokale Prüfung sicherzustellen.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
