# Technische Referenz — Member Directory v0.3.0 (Éclair v2.0.0, experimenteller POST-Vertrag)

## Verfügbare Abläufe (alle cache:false)

| Methode | Route | Rolle |
|---|---|---|
| GET/POST | `/membres/connexion` | Formular / Anmeldung eines aktiven Kontos |
| GET | `/membres/espace` | Privates Profil, das zum Sitzungstoken gehört |
| POST | `/membres/deconnexion` | Abmeldung mit sitzungseigenem CSRF |
| GET/POST | `/membres/inscription` | Einladungs-E-Mail, nur wenn `registration_enabled=true` |
| GET/POST | `/membres/verification` | Passwort mit einmaligem E-Mail-Nachweis wählen |
| GET/POST | `/membres/recuperation` | Wiederherstellungs-E-Mail anfordern, wenn `recovery_enabled=true` |
| GET/POST | `/membres/reinitialisation` | Passwort mit einmaligem Nachweis ersetzen |

## Mechanismen

- Kein CMS-Konto/`Auth::can` für Kunden. Die Profile `member` enthalten niemals die Rollen `admin` oder `editor`.
- `MemberAccounts::provision` verlangt ein zufälliges vorläufiges Passwort und erstellt ein Konto `pending`. Der Link in der E-Mail fordert die Person auf, ihr eigenes Passwort zu wählen. Das Verifizierungstoken läuft nach 30 Minuten ab, und eine Quittung lässt sich nur einmal verwenden.
- `MemberAccounts::issueReset` stellt nur für ein Mitglied im Zustand `active` aus, anschließend führt `confirmReset` die Änderung unter Sperre durch und erhöht `epoch`. Alle alten Sitzungstoken werden ungültig.
- `Mail::send` (Éclair-Dienst) wird verwendet, ist aber keine Zustellbestätigung. Dem Benutzer keinerlei Zustellerfolg versprechen.
- Um eine E-Mail zu senden, muss die konfigurierte kanonische URL HTTPS verwenden und verifiziert sein. Die Domain der HTTP-Anfrage ist vom Wiederherstellungslink ausgeschlossen.
- GET-Seiten führen keinerlei Geschäftslogik aus; POST erfordert HTTPS und `Security::checkFormToken`, wobei der Kern-Patch diese Bedingungen ebenfalls prüft.
- Begrenzer pro Netzwerk / E-Mail, generische Meldungen bei Anfragen, zweifach validierte Nachweise (Preflight vor dem Hash, dann unter Speichersperre).
- Keine persönliche Ressource gelangt in den öffentlichen statischen Cache. Links mit Token müssen von den Protokollen ausgeschlossen werden, ebenso jede externe Seite, die aus den Bestätigungsformularen geladen wird.

## Ausdrückliche Grenzen

- Ein ausstehendes Konto, dessen E-Mail vom Transport angenommen, aber nie empfangen wurde, benötigt einen Ablauf für erneute Einladung/Support, der hier nicht bereitgestellt wird.
- Generische Meldungen beseitigen nicht vollständig die Möglichkeit, die Existenz eines Kontos aus der Ausführungsdauer abzuleiten.
- E-Mail-Token in der URL können im Browserverlauf oder in Logs erscheinen: Audit der Infrastruktur zwingend erforderlich.
- Der `Store`-Prototyp ist auf 1 000 Mitglieder begrenzt und ist keine transaktionale relationale Datenbank über mehrere Dateien.
- Der offizielle Vertrag `eclair-extension/1` erlaubt öffentliches POST ohne Patch **nicht**. Jede Installation auf einer echten Website wartet auf dessen Validierung.
