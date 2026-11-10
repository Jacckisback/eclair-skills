# Validierungsplan — Suche auf der Website

## Datenmodell
Index der veröffentlichten Inhalte, Titel, Auszug, Adresse.

## Erwartete Umsetzung
Per geplanter Aufgabe einen statischen Index der öffentlichen Inhalte erzeugen, ihn per cachefähigem GET ausliefern und im Browser suchen, mit einer Ausweichseite ohne JavaScript.

## Vorzusehende Tests
1. Normalfall: Einen vorhandenen, einen fehlenden und einen Begriff mit Akzenten suchen und die Antwortzeit prüfen.
2. Ablehnungskontrolle: Ein Entwurf oder eine private Seite erscheint niemals im Index.
3. Invariante: Der Index enthält nur öffentliche Inhalte; keine Besucheranfrage wird mit der Identität des Besuchers protokolliert.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
