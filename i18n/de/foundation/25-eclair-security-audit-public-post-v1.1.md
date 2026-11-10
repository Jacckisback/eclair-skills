# Public member HTTP routes — Éclair 2.0.0 experimental

Der Prototyp v1.1 hat eine Begrenzung per `RateLimit::attempt` vor dem Hashing, eine strikte Trennung zwischen Mitgliedern und Admins sowie Sitzungstoken mit 256 Bit. Die Sicherheit von `Origin`, von TLS hinter einem Reverse Proxy, CSRF, IDOR, Konten-Enumeration, Informationslecks und Nebenläufigkeit bewerten. Isolierte Tests nicht mit einem Audit in Produktion verwechseln.

Der Quell-Patch liegt in `core-patch/` der vollständigen Distribution und ist in einer eigenständigen Kopie des Skills nicht enthalten. Diesen Patch niemals als offizielle API betrachten, bevor er upstream gemergt ist.
