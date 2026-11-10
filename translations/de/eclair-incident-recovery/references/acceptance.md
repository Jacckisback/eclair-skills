# Validierungsplan — Reaktion auf Vorfälle

## Datenmodell
Vorfall, Chronologie, betroffene Konten, saubere Sicherung.

## Erwartete Umsetzung
Isolieren, die Beweise sichern, die Secrets ändern, die Integrität prüfen, eine saubere Sicherung wiederherstellen, bei Bedarf die betroffenen Personen informieren.

## Vorzusehende Tests
1. Normalfall: Die Übung auf einer Kopie durchspielen: Erkennung, Wiederherstellung, Kontrolle.
2. Ablehnungskontrolle: Eine wiederhergestellte Website geht nicht wieder online, bevor alle Secrets geändert wurden.
3. Invariante: Niemals die Spuren löschen, bevor sie kopiert wurden.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
