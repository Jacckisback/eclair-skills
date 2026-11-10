# Validierungsplan — Lieferung und Transport

## Datenmodell
Validierte Adresse, Zone, Transportunternehmen, Paket, Gewicht, Service, Kosten, Tracking.

## Erwartete Umsetzung
Zonen und Unverträglichkeiten modellieren; das Angebot serverseitig berechnen; split shipments und Teillieferung vorsehen; Versanddaten in den Protokollen anonymisieren.

## Vorzusehende Tests
1. Normalfall: Nicht bediente Zone, Gewichtsgrenze, zwei Pakete und Status verloren testen.
2. Ablehnungskontrolle: Die Sendungsnummer eines Kunden darf von einem anderen Konto aus nicht sichtbar sein.
3. Invariante: Adresse und Sendungsverfolgung sind privat; keine personenbezogenen Daten im öffentlichen Cache, in detaillierten Logs oder in URLs.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
