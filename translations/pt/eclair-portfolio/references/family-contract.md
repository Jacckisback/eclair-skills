# Contrato da família Aplicações de negócio

Alvo: **Éclair CMS 2.0.x**, extensão **`eclair-extension/1`**, identificadores e versão descobertos antes de qualquer modificação.

**Capacidades nativas a privilegiar:** funcionalidades já integradas no núcleo (ver `core-map.md`), temas em `site/themes/`, extensões em `site/extensions/`, dados `Store` sob `$ctx['data']`, rotas GET públicas e GET/POST de administração protegidas, tarefas agendadas, migrações, validação `tools/validate.php`, suite PHP, medições.

**Limitações de produção:** As montras públicas são possíveis com GET; reservas, pagamentos, candidaturas, CRM e dados pessoais exigem POST seguro, armazenamento adequado e permissões verificadas do lado do servidor.

**Política do agente:** utilizar primeiro o nativo, gerar o mínimo de código, manter o núcleo intacto, recusar apresentar uma maqueta como uma funcionalidade em serviço; pedir uma evolução do núcleo quando for necessária. As alterações de grande alcance (pagamento, conteúdo privado, e-mails, dados pessoais ou de saúde) exigem testes reais e uma validação humana antes da ativação.

**Pontos de segurança:** controlar cada objeto e cada escrita; proteger formulários, segredos, assinaturas e dados pessoais; verificar erros e reversão; manter em cache pública apenas HTML sem dados de utilizador. Não confundir `eclair-extension/1` com as API experimentais anteriores.
