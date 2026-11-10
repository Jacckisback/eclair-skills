# Validierungsplan — Gruppen

## Datenmodell
Gruppe, Sichtbarkeit, Mitglieder, Rollen.

## Erwartete Umsetzung
Erstellung, Beitritt, Rollen und Sichtbarkeit festlegen; die Rechte bei jedem Lesezugriff anwenden.

## Vorzusehende Tests
1. Normalfall: Erstellung, Beitrittsanfrage und Ausschluss simulieren.
2. Ablehnungskontrolle: Ein Nichtmitglied liest keinen Inhalt einer privaten Gruppe.
3. Invariante: Der Inhalt einer privaten Gruppe erscheint weder in der Suche noch im öffentlichen Cache.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
