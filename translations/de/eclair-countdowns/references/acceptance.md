# Validierungsplan — Countdowns

## Datenmodell
Zieldatum, Zeitzone, Abschlussmeldung.

## Erwartete Umsetzung
Das Datum ins HTML schreiben, als Progressive Enhancement animieren, den Zustand nach Fristablauf und die Cache-Invalidierung vorsehen.

## Vorzusehende Tests
1. Normalfall: Vor, während und nach dem Fristablauf sowie in zwei Zeitzonen testen.
2. Ablehnungskontrolle: Nach dem Fristablauf zeigt die Seite aus dem Cache kein abgelaufenes Angebot mehr an.
3. Invariante: Keine falsche Dringlichkeit: Das Datum entspricht einem echten Ereignis.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
