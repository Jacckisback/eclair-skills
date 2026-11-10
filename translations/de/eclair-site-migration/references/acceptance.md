# Validierungsplan — Wechsel des Hosters oder der Domain

## Datenmodell
Sicherung, neues Hosting, DNS, Domain-Weiterleitungen.

## Erwartete Umsetzung
Sichern, beim neuen Hoster wiederherstellen, prüfen, das DNS umstellen, die alte Domain Seite für Seite weiterleiten.

## Vorzusehende Tests
1. Normalfall: Den Umzug auf einer Testdomain proben.
2. Ablehnungskontrolle: Keine alte Adresse antwortet nach der Umstellung mit 404.
3. Invariante: Die Secrets der Website werden niemals per E-Mail oder Messenger übermittelt.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
