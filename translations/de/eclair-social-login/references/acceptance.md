# Validierungsplan — Anmeldung über Drittkonto

## Datenmodell
Identitätsanbieter, verknüpftes Konto, Einwilligung.

## Erwartete Umsetzung
Hängt zunächst von Mitgliedskonten ab; den OAuth-Ablauf mit State, PKCE und ausdrücklicher Kontoverknüpfung konzipieren.

## Vorzusehende Tests
1. Normalfall: Anmeldung, Verknüpfung und Aufhebung der Verknüpfung simulieren.
2. Ablehnungskontrolle: Eine wiederholt eingespielte oder gefälschte OAuth-Antwort wird abgelehnt.
3. Invariante: Kein Konto wird allein im Vertrauen auf eine nicht verifizierte E-Mail-Adresse zusammengeführt.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
