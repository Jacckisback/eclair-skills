# Validierungsplan — Zwei-Faktor-Authentifizierung

## Datenmodell
Konto, TOTP-Secret, Notfallcodes.

## Erwartete Umsetzung
Die Zwei-Faktor-Authentifizierung von jeder Person aktivieren lassen, die Notfallcodes sicher verwahren, den Geräteverlust einplanen.

## Vorzusehende Tests
1. Normalfall: Aktivieren, abmelden, mit dem zweiten Faktor wieder anmelden.
2. Ablehnungskontrolle: Ein korrektes Passwort ohne zweiten Faktor gewährt keinen Zugriff.
3. Invariante: Die Secrets und Notfallcodes werden niemals in einen Chat, eine E-Mail oder ein Repository kopiert.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
