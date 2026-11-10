# Validierungsplan — Termine und Kalender

## Datenmodell
Anbieter, Leistung, Dauer, Puffer, Ausnahmen, Ereignisse und Zeitzonen.

## Erwartete Umsetzung
Zeiten in UTC normalisieren, Anzeigezeitzone beibehalten, nicht verfügbare Zeitfenster sperren, externe Neusynchronisierung verwalten.

## Vorzusehende Tests
1. Normalfall: DST, Termin über Mitternacht hinweg, gelöschtes Ereignis testen.
2. Ablehnungskontrolle: Ein manuell gesperrtes Zeitfenster wird nach einer Neusynchronisierung niemals angeboten.
3. Invariante: Eine externe Integration erfordert OAuth/minimale Scopes und darf die privaten Kalender nicht offenlegen.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
