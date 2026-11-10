# Public member HTTP routes — Éclair 2.0.0 experimental

Der Prototyp v1.1 besitzt öffentliche Handler: GET für das Formular + POST für Anmeldung/Abmeldung + GET für den privaten Bereich. Sie sind erst nach der genehmigten Aufnahme des POST-Vertrags gültig. Mitgliedersitzungen getrennt von denen der Admins, opakes Token, Double-Submit-CSRF und Sitzungs-CSRF bei der Abmeldung; keine Rolle admin/editor wird vergeben.

Der Quell-Patch liegt in `core-patch/` der vollständigen Distribution und ist in einer eigenständigen Kopie des Skills nicht enthalten. Diesen Patch niemals als offizielle API betrachten, bevor er upstream gemergt ist.
