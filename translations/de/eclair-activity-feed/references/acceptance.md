# Validierungsplan — Aktivitäts-Feed

## Datenmodell
Ereignis, Autor, Sichtbarkeit, Datum.

## Erwartete Umsetzung
Festlegen, welche Ereignisse veröffentlicht werden, für wen, und wie ein Mitglied sie ausblendet oder löscht.

## Vorzusehende Tests
1. Normalfall: Veröffentlichungen mit unterschiedlicher Sichtbarkeit simulieren.
2. Ablehnungskontrolle: Ein gelöschter Inhalt verschwindet auch aus dem Feed.
3. Invariante: Keine private Aktivität wird in einem öffentlichen Feed preisgegeben.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
