# Éclair Member Directory — v1.0 reference

Ein nativer Demonstrator für Éclair 2.0 liegt in `examples/extensions/member-directory/` im Wurzelverzeichnis der Quelldistribution; er ist bei der eigenständigen Kopie des Skills nicht enthalten.

- `schema`: `eclair-extension/1`; `requires.eclair`: `>=2.0.0`.
- Routen `admin`: GET auf die Wurzel, POST `/create`, POST `/disable`; Recht `users`.
- Keine öffentliche Route. Kein öffentlicher Login, und es wird keine Bestätigungs-E-Mail versendet.
- `Store`: Schlüssel `ext/member-directory/...`, Schreiben unter Sperre, Grenze von 1 000 Mitgliedern zu Versuchszwecken.
- Mitgliedersitzung getrennt von den Sitzungen der Administration, opakes 256-Bit-Token, im Ruhezustand gehasht, Widerruf per Epoch.
- Aktivierung nach E-Mail-Nachweis: wird von der HTTP-Oberfläche nicht bereitgestellt. Eine Mitgliederrolle kann nicht `admin` oder `editor` sein.
- Installation: die Erweiterung nach `site/extensions/member-directory` kopieren, `tools/validate.php` des Kerns 2.0 durchlaufen lassen, nur im Labor manuell importieren und aktivieren.
- Für aktive, für die Öffentlichkeit bestimmte Konten: RFC für sicheres öffentliches POST, E-Mail-Validierung, Rate Limiting, Reset-Ablauf und native Tests. Keine GET-Route darf ein Konto oder eine Sitzung erstellen/ändern.
