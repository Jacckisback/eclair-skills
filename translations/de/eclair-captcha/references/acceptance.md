# Validierungsplan — Captcha

## Datenmodell
Challenge, Token, Serverprüfung.

## Erwartete Umsetzung
Honeypot-Feld und native Limits bevorzugen; ein Drittanbieter-Captcha erfordert eine Öffnung der Inhaltsrichtlinie, die der Kern nicht an Erweiterungen delegiert.

## Vorzusehende Tests
1. Normalfall: Prüfen, dass der gewählte Schutz eine automatisierte Einsendung blockiert.
2. Ablehnungskontrolle: Auf Seiten ohne Formular wird kein Captcha-Skript geladen.
3. Invariante: Niemals die Content-Security-Policy der Website schwächen, um ein Drittanbieter-Skript zu laden.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
