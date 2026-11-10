# Validierungsplan — Kalender-Feeds

## Datenmodell
Ereignis, Datum, Zeitzone, Ort, iCalendar-Feed.

## Erwartete Umsetzung
Aus den veröffentlichten Ereignissen einen öffentlichen iCalendar-Feed per GET erzeugen, mit ausdrücklichen Zeitzonen.

## Vorzusehende Tests
1. Normalfall: Den Feed aus zwei Kalenderanwendungen abonnieren.
2. Ablehnungskontrolle: Ein abgesagtes Ereignis ist im Feed als abgesagt gekennzeichnet.
3. Invariante: Der Feed enthält nur öffentliche Ereignisse, ohne Teilnehmer.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
