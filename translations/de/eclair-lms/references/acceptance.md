# Validierungsplan — LMS-Architektur

## Datenmodell
Kurse, Abschnitte, Lektionen, Voraussetzungen, Einschreibungen, Fortschritt, Rechte und eventuelle Verkäufe.

## Erwartete Umsetzung
Öffentliche Kataloge vs. private Lektionen festlegen; einen transaktionalen Fortschrittsspeicher wählen; Zugriff an die validierte Mitgliedsidentität binden; unabhängige Module zusammenstellen.

## Vorzusehende Tests
1. Normalfall: Lernenden, Lehrenden, Administrator und Besucher testen.
2. Ablehnungskontrolle: Ein eingeschriebener Lernender kann den privaten Inhalt eines anderen Kurses nicht lesen.
3. Invariante: Kein Versprechen eines privaten Zugriffs über eine bloße geheime URL oder einen versteckten Block.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
