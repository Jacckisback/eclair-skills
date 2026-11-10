# Validierungsplan — Transaktionale E-Mails

## Datenmodell
Template, Sprache, Einwilligung, Empfänger, Domain, Ereignis, Zustellung.

## Erwartete Umsetzung
Text-/HTML-Vorlagen, DKIM/SPF/DMARC und Zustellbarkeit vorbereiten; Transaktionales und Marketing unterscheiden, Protokoll ohne Secrets, Abmeldung erforderlich.

## Vorzusehende Tests
1. Normalfall: SMTP-Fehler, Adressfehler, Wiederaufnahme und Ablauf des Tokens testen.
2. Ablehnungskontrolle: Ein SMTP-Fehlschlag markiert eine E-Mail nicht als zugestellt und sperrt ein Konto nicht dauerhaft.
3. Invariante: Kein Wiederherstellungstoken über eine nicht verifizierte URL senden; niemals Spam ohne Einwilligung.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
