# Validierungsplan — Datenschutzanfragen

## Datenmodell
Anfrage, Person, betroffene Daten, Frist, Antwort.

## Erwartete Umsetzung
Erfassen, wo die Daten liegen (Nachrichten, Konten, Protokolle, Sicherungen), das Verfahren für Auskunft und Löschung schreiben, ein Verzeichnis führen.

## Vorzusehende Tests
1. Normalfall: Eine Auskunftsanfrage und dann eine Löschanfrage auf einem Testdatensatz durchspielen.
2. Ablehnungskontrolle: Eine Anfrage ohne Identitätsprüfung führt zu keiner Offenlegung.
3. Invariante: Die Identität des Anfragenden wird vor jeder Herausgabe von Daten geprüft.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
