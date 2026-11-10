# Validierungsplan — Mediathek

## Datenmodell
Datei, Alternativtext, Abmessungen, Verwendungen.

## Erwartete Umsetzung
Die Medien importieren, die Alternativtexte ausfüllen, ungenutzte Dateien und Duplikate aufspüren.

## Vorzusehende Tests
1. Normalfall: Mehrere Formate hochladen und Konvertierung, Abmessungen und Alternativtexte prüfen.
2. Ablehnungskontrolle: Eine Datei in einem verbotenen Format oder eine präparierte Datei wird beim Hochladen abgelehnt.
3. Invariante: Nur die vom Kern akzeptierten Formate werden hochgeladen; keine ausführbare Datei.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
