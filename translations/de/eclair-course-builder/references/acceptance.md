# Validierungsplan — Erstellung von Lernpfaden

## Datenmodell
Kurs, Modul, Lektion, Reihenfolge, Entwurf, veröffentlichte Version und Autor.

## Erwartete Umsetzung
Hierarchisches Schema aufstellen; vor der Veröffentlichung in der Vorschau prüfen; Kennungen beim Umsortieren erhalten; Archivierung dokumentieren.

## Vorzusehende Tests
1. Normalfall: Vertauschen von Lektionen, Zurückziehen der Veröffentlichung und gleichzeitige Bearbeitung testen.
2. Ablehnungskontrolle: Das Ändern der Reihenfolge setzt den Fortschritt der Lernenden nicht zurück.
3. Invariante: Die Entwürfe von Lehrenden dürfen nicht indexiert oder öffentlich zugänglich gemacht werden.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
