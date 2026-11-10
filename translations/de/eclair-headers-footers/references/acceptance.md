# Validierungsplan — Kopf- und Fußbereiche

## Datenmodell
Logo, Menü, Kontaktdaten, rechtliche Links.

## Erwartete Umsetzung
Über ein Theme-Paket in site/themes gehen, die Variablen des Theme-Vertrags einhalten, Sprunglink und rechtliche Links beibehalten.

## Vorzusehende Tests
1. Normalfall: Das Theme validieren und Kopf- und Fußbereich auf allen Seitentypen prüfen.
2. Ablehnungskontrolle: Das vom Validator abgelehnte Theme wird nicht ausgeliefert.
3. Invariante: Niemals selbst SEO-Tags oder Header erzeugen, die der Kern bereits liefert.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
