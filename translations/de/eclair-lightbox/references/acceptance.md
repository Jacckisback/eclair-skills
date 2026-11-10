# Validierungsplan — Bildbetrachter

## Datenmodell
Bild, vergrößerte Version, Bildunterschrift.

## Erwartete Umsetzung
Natives dialog oder einen Link zum Bild verwenden, Fokus, Escape-Taste und Zurück behandeln, ohne Abhängigkeit.

## Vorzusehende Tests
1. Normalfall: Per Tastatur öffnen, navigieren und schließen.
2. Ablehnungskontrolle: Ohne JavaScript öffnet der Klick einfach das Bild.
3. Invariante: Der Fokus wird gefangen und dann korrekt zurückgegeben; kein externer Inhalt.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
