# Validierungsplan — Audio und Podcast

## Datenmodell
Folge, Audiodatei, Dauer, Notizen, Feed.

## Erwartete Umsetzung
Pro Folge eine Seite mit nativem HTML-Player anlegen, den Podcast-Feed per GET erzeugen und große Dateien bei Bedarf außerhalb der Website hosten.

## Vorzusehende Tests
1. Normalfall: Den Feed mit einem Podcast-Validator validieren und eine Folge auf dem Mobilgerät abspielen.
2. Ablehnungskontrolle: Eine Folge im Entwurf fehlt im Feed.
3. Invariante: Der Feed verweist nur auf veröffentlichte Folgen und öffentliche Dateien.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
