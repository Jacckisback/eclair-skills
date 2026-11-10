# Public member HTTP routes — Éclair 2.0.0 experimental

Der Speicher des Demonstrators nutzt weiterhin die geschützten Dateien von `Store` und eine globale Sperre. Er ist auf 1000 Konten begrenzt; kein Versprechen von Atomarität über mehrere Dateien, von Zugriff in großem Maßstab oder von transaktionaler Ausfallsicherheit. Ein SQL-Backend ist Voraussetzung vor jedem geschäftlichen Einsatz.

Der Quell-Patch liegt in `core-patch/` der vollständigen Distribution und ist in einer eigenständigen Kopie des Skills nicht enthalten. Diesen Patch niemals als offizielle API betrachten, bevor er upstream gemergt ist.
