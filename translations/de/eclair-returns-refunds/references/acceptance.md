# Validierungsplan — Rücksendungen und Erstattungen

## Datenmodell
Rücksendeanfrage, Grund, Zustand, Erstattung.

## Erwartete Umsetzung
Die native Rückgaberichtlinie auf den Produktseiten veröffentlichen, die Anfragen über das Kontaktformular bearbeiten, beim Dienstleister erstatten; die strukturierte Nachverfolgung konzipieren.

## Vorzusehende Tests
1. Normalfall: Eine Rücksendeanfrage vom Eingang bis zur Erstattung durchspielen.
2. Ablehnungskontrolle: Eine Anfrage nach Fristablauf erhält eine begründete Antwort, keine automatische Erstattung.
3. Invariante: Eine Erstattung wird nur von einer befugten Person beim Dienstleister ausgelöst.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
