# Validierungsplan — Benutzerdefinierte Inhaltstypen

## Datenmodell
Fachdatensatz, Felder, Liste, Adresse, Status.

## Erwartete Umsetzung
Zwischen Seiten mit eigenen Blöcken und einer Erweiterung mit eigener Speicherung und GET-Routen wählen, die Adressen festlegen, Liste und Detailansicht vorsehen.

## Vorzusehende Tests
1. Normalfall: Einen Datensatztyp per Erweiterung anlegen, mit Liste und Detail per GET, dann das Paket validieren.
2. Ablehnungskontrolle: Ein nicht veröffentlichter Datensatz wird weder in der Liste noch über seine direkte Adresse ausgeliefert.
3. Invariante: Niemals aus einer Erweiterung heraus in die Inhaltsdateien des Kerns schreiben.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
