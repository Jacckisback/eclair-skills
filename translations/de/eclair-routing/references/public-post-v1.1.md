# Public member HTTP routes — Éclair 2.0.0 experimental

Öffentliche POST-Routen sind im offiziellen Éclair 2.0 **nicht** vorhanden. Der vorgeschlagene Patch v1.1 macht eine kontrollierte Ausnahme: explizite Methode POST, `cache:false`, HTTPS, `Security::checkFormToken()`, Antwort `private,no-store`, relative 303-Weiterleitung. Vor dem Mergen immer HTTP-Tests mit dem vollständigen CMS durchführen.

Der Quell-Patch liegt in `core-patch/` der vollständigen Distribution und ist in einer eigenständigen Kopie des Skills nicht enthalten. Diesen Patch niemals als offizielle API betrachten, bevor er upstream gemergt ist.
