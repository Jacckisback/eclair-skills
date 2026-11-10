# Public member HTTP routes — Éclair 2.0.0 experimental

Öffentliche GET-Formulare verwenden `Security::formField()` und müssen mit `cache:false` deklariert werden. Ihre Antworten dürfen den Fast Path des Kerns nicht erreichen. POST ist vom Fast Path ausgeschlossen und wird auf no-store gezwungen. Die Bereinigung des Caches bei der Aktivierung des Moduls testen und prüfen, dass im HTML des gemeinsamen Caches keine Cookies/Identitäten enthalten sind.

Der Quell-Patch liegt in `core-patch/` der vollständigen Distribution und ist in einer eigenständigen Kopie des Skills nicht enthalten. Diesen Patch niemals als offizielle API betrachten, bevor er upstream gemergt ist.
