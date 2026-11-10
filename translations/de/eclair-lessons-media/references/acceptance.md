# Validierungsplan — Lernmedien

## Datenmodell
Lektion, Medium, Transkript, herunterladbare Dateien, Rechte und Dauer.

## Erwartete Umsetzung
Barrierefreie Medien und Untertitel vorbereiten; Auslieferung mit serverseitiger Autorisierung oder kurzlebiger signierter URL vorsehen; öffentliches CDN und vorbehaltenen Inhalt trennen.

## Vorzusehende Tests
1. Normalfall: Abgelaufenes Medium, Zugriff ohne Einschreibung und Mobilgerät testen.
2. Ablehnungskontrolle: Eine in einen anderen Browser kopierte URL eines privaten Dokuments wird abgelehnt oder läuft ab.
3. Invariante: Einen Link im HTML zu verbergen ist kein Schutz; das private Medium nicht im öffentlichen /media ablegen.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
