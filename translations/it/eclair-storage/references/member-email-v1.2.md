# Riferimento tecnico — Member Directory v0.3.0 (Éclair v2.0.0, contratto POST sperimentale)

## Percorsi disponibili (tutti cache:false)

| Metodo | Route | Ruolo |
|---|---|---|
| GET/POST | `/membres/connexion` | Modulo / accesso di un account attivo |
| GET | `/membres/espace` | Profilo privato proprio del token di sessione |
| POST | `/membres/deconnexion` | Disconnessione con CSRF proprio della sessione |
| GET/POST | `/membres/inscription` | Email di invito, solo se `registration_enabled=true` |
| GET/POST | `/membres/verification` | Scegliere la password con prova email monouso |
| GET/POST | `/membres/recuperation` | Richiedere un'email di recupero se `recovery_enabled=true` |
| GET/POST | `/membres/reinitialisation` | Sostituire la password con prova monouso |

## Meccanismi

- Nessun account CMS/`Auth::can` per i clienti. I profili `member` non contengono mai ruoli `admin` o `editor`.
- `MemberAccounts::provision` richiede una password provvisoria casuale e crea un account `pending`. Il link nell'email chiede alla persona di scegliere la propria password. Il token di verifica scade dopo 30 minuti e una ricevuta si usa una sola volta.
- `MemberAccounts::issueReset` emette unicamente per un membro `active`, poi `confirmReset` esegue la mutazione sotto lock e incrementa `epoch`. Tutti i vecchi token di sessione diventano non validi.
- `Mail::send` (servizio Éclair) viene utilizzato, ma non è una conferma di consegna. Non promettere all'utente alcun successo di consegna.
- Per inviare un'email, l'URL canonico configurato deve essere HTTPS e verificato. Il dominio della richiesta HTTP è escluso dal link di recupero.
- Le pagine GET non eseguono alcuna elaborazione di business; il POST richiede HTTPS e `Security::checkFormToken`, e anche la patch del core verifica queste condizioni.
- Limitatori per rete / email, messaggi generici sulle richieste, prove validate due volte (preflight prima dell'hash, poi sotto lock di storage).
- Nessuna risorsa personale passa nella cache statica pubblica. I link con token devono essere esclusi dai log e da qualsiasi pagina esterna caricata dai moduli di conferma.

## Limiti espliciti

- Un account in attesa la cui email è accettata dal trasporto ma mai ricevuta richiede un percorso di nuovo invito/assistenza, non fornito qui.
- I messaggi generici non eliminano del tutto la possibilità di dedurre l'esistenza di un account dal tempo di esecuzione.
- I token email nell'URL possono comparire nella cronologia del browser o nei log: audit dell'infrastruttura obbligatorio.
- Il prototipo `Store` è limitato a 1 000 membri e non è un database relazionale transazionale multi-file.
- Il contratto `eclair-extension/1` ufficiale **non** autorizza il POST pubblico senza patch. Qualsiasi installazione su un sito reale è subordinata alla sua validazione.
