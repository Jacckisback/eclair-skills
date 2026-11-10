# Validierungsplan — Portierung von WordPress-Erweiterungen

## Datenmodell
Ursprüngliche Erweiterung, tatsächlich genutzte Funktionen, natives Äquivalent, Abweichung.

## Erwartete Umsetzung
Auflisten, was die Erweiterung auf der Website wirklich tut, zuerst die native Funktion suchen, andernfalls den skill aus dem Katalog, andernfalls eine maßgeschneiderte Erweiterung; niemals PHP-Code von WordPress kopieren.

## Vorzusehende Tests
1. Normalfall: Die Zuordnungstabelle einer echten Website erstellen und freigeben lassen.
2. Ablehnungskontrolle: Eine Funktion ohne Äquivalent wird als fehlend gemeldet, nicht simuliert.
3. Invariante: Kein Code unter inkompatibler Lizenz oder mit Abhängigkeit von der WordPress-API wird übernommen.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
