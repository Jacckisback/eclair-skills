# Validierungsplan — Brotkrumennavigation

## Datenmodell
Ebenen, Beschriftungen, Adressen.

## Erwartete Umsetzung
Die Übereinstimmung zwischen Seitenstruktur, angezeigter Brotkrumennavigation und strukturierten Daten des Kerns kontrollieren.

## Vorzusehende Tests
1. Normalfall: Angezeigte Brotkrumennavigation und Markup über drei Ebenen Tiefe vergleichen.
2. Ablehnungskontrolle: Eine verwaiste Seite zeigt keine widersprüchliche Brotkrumennavigation an.
3. Invariante: Die Brotkrumennavigation verrät keine nicht veröffentlichte Seite.
4. GET/HEAD: öffentlicher Cache nur ohne Sitzungszustand und ohne sensible Daten; Canonical, HTTP-Status, SEO und GEO unverändert oder verbessert.
5. POST: niemals gemeinsamer Cache; CSRF, TLS, Berechtigungen, Begrenzung der Versuche, Idempotenz. Nicht ausführen, wenn der Kern es nicht offiziell unterstützt.
6. Aktivierung und Deaktivierung: Die Inhalte bleiben erhalten und die öffentlichen Routen werden ohne Datenleck entfernt.
7. Kontrollen: nativer Validator, PHP- und HTTP-Tests, Budgets; die ausgeführten Befehle, ihre Ergebnisse und das, was nicht getestet wurde, festhalten.

## Verfügbarkeitsnachweis
Zustand der Funktion oder der Erweiterung, CI-Protokolle, Testmatrix, Rollback-Verfahren und Ablehnung jedes ungeprüften Versprechens.
