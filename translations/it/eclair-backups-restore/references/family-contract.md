# Contratto della famiglia Amministrazione e manutenzione

Target: **Éclair CMS 2.0.x**, estensione **`eclair-extension/1`**, identificativi e versione rilevati prima di qualsiasi modifica.

**Capacità native da privilegiare:** funzioni già integrate nel core (vedere `core-map.md`), temi in `site/themes/`, estensioni in `site/extensions/`, dati `Store` sotto `$ctx['data']`, route GET pubbliche e GET/POST di amministrazione protette, task pianificati, migrazioni, validazione `tools/validate.php`, suite PHP, misure.

**Limitazioni di produzione:** Backup, ripristino, aggiornamento firmato e registro sono nativi; le azioni sensibili richiedono il permesso Sicurezza e la password della persona, mai di un agente da solo.

**Politica per l'agente:** usare prima il nativo, generare il minimo di codice, mantenere intatto il core, rifiutare di presentare un mockup come una funzionalità in servizio; richiedere un'evoluzione del core quando è necessaria. Le modifiche ad ampio impatto (pagamento, contenuto privato, email, dati personali o sanitari) richiedono test reali e una validazione umana prima dell'attivazione.

**Punti di sicurezza:** controllare ogni oggetto e ogni scrittura; proteggere moduli, segreti, firme e dati personali; verificare errori e rollback; mantenere in cache pubblica soltanto HTML privo di dati dell'utente. Non confondere `eclair-extension/1` con le API sperimentali precedenti.
