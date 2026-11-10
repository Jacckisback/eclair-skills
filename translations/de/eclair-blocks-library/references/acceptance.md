# Validierungsplan — Block-Bibliothek

## Datenmodell
Typ mit Namespace, Deklaration der Felder, Grenzen, Ausgabe und beibehaltene Daten.

## Erwartete Umsetzung
Native Blöcke bevorzugen; zulässige Felder deklarieren; escapte Ausgabe, Standardwerte und Datenerhalt nach der Deaktivierung erzeugen.

## Vorzusehende Tests
1. Normalfall: Ungültige Felder, Entfernen der Erweiterung und Neuinstallation testen.
2. Ablehnungskontrolle: Der deaktivierte Block bleibt erhalten, wird aber weder ausgeführt noch ausgegeben.
3. Invariante: Die Ausführung von HTML/JS aus Feldern ablehnen; kein Datenverlust, wenn der Block fehlt.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
