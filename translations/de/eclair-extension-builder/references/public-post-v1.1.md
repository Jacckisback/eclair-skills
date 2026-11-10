# Public member HTTP routes — Éclair 2.0.0 experimental

Ein Prototyp einer öffentlichen POST-Route befindet sich in `examples/extensions/member-directory/`. Er wird vom offiziellen Kern 2.0 abgelehnt. Das Manifest nur mit dem experimentellen Patch und der ausdrücklichen Zustimmung eines Maintainers verwenden, niemals in Produktion. POST erfordert `cache:false`, TLS, CSRF und eine relative Weiterleitung.

Der Quell-Patch liegt in `core-patch/` der vollständigen Distribution und ist in einer eigenständigen Kopie des Skills nicht enthalten. Diesen Patch niemals als offizielle API betrachten, bevor er upstream gemergt ist.
