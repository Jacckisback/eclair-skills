# Validierungsplan — Updates und Rollback

## Datenmodell
Installierte Version, angekündigte Version, Signatur, Rücksetzpunkt.

## Erwartete Umsetzung
Sichern, die Versionshinweise lesen, das Update mit einem Klick starten, die Website prüfen, zur vorherigen Version zurückkehren können.

## Vorzusehende Tests
1. Normalfall: Eine Kopie der Website aktualisieren und dann zurücksetzen.
2. Ablehnungskontrolle: Eine nicht vom Maintainer signierte Update-Ankündigung wird abgelehnt.
3. Invariante: Niemals ein Archiv installieren, dessen Signatur nicht vom Kern verifiziert ist.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
