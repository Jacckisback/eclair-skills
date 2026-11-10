# Validierungsplan — Öffentliche Lese-API

## Datenmodell
Ressource, öffentliche Felder, Paginierung, Version.

## Erwartete Umsetzung
Cachebare GET-Routen deklarieren, die begrenztes und versioniertes JSON zurückgeben; dokumentieren, dass das Schreiben nicht geöffnet ist.

## Vorzusehende Tests
1. Normalfall: Liste und Detail, Paginierung und Leerfall lesen.
2. Ablehnungskontrolle: Ein nicht veröffentlichter Inhalt wird von keiner Route zurückgegeben.
3. Invariante: Nur bereits öffentliche Inhalte werden bereitgestellt; keine sensible interne Kennung.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
