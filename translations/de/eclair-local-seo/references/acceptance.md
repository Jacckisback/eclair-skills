# Validierungsplan — Lokale Suchmaschinenoptimierung

## Datenmodell
Name, Adresse, Telefon, Öffnungszeiten, Einzugsgebiet.

## Erwartete Umsetzung
Die exakten Kontaktdaten in den Einstellungen eintragen, das vom Kern erzeugte Markup für lokale Unternehmen prüfen, Unternehmensprofil und Website abgleichen.

## Vorzusehende Tests
1. Normalfall: Kontaktdaten der Website, des Markups und des Unternehmensprofils vergleichen.
2. Ablehnungskontrolle: Nicht bestätigte Öffnungszeiten werden nicht veröffentlicht.
3. Invariante: Keine erfundene Adresse, Bewertung oder kein erfundenes Einsatzgebiet.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
