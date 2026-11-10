---
name: eclair-email-marketing-providers
description: "Ligar o site a um serviço de email marketing (Brevo, Mailchimp ou outro). Use on Éclair CMS 2.x when the user wants to: ligar o site a um serviço de e-mail marketing (Brevo, Mailchimp ou outro). Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Serviços de e-mail marketing — Éclair CMS 2.x

## Desencadeador e resultado esperado
Utilizar este skill para **ligar o site a um serviço de e-mail marketing (Brevo, Mailchimp ou outro)**. Esta funcionalidade está **em parte bloqueada pelo contrato do núcleo**: o skill entrega o que é nativo e documenta a lacuna. Este skill é um **workflow de agente**, não uma extensão PHP funcional nem uma garantia de conformidade.

**Equivalente WordPress:** Extensões oficiais Brevo ou Mailchimp. Família: Integrações e automação.

## Diagnóstico obrigatório antes de qualquer modificação
1. Ler `references/core-map.md` (o que o núcleo já faz) e `references/native-contract.md`; verificar a versão real do CMS e as capacidades em `GET /<admin>/api/capabilities` (se o acesso for autorizado).
2. Ler `references/family-contract.md` e `references/acceptance.md`. Nunca copiar o antigo sistema de packs v0.x nem código PHP do WordPress para o Éclair 2.
3. Identificar o modelo de dados: **Lista, formulário alojado, chave de API, sincronização**. Documentar o que é público, o que é privado e de onde vem cada dado.

## Procedimento específico
4. **Percurso:** Utilizar o formulário alojado do serviço; guardar qualquer chave de API nos segredos da extensão; sincronizar por tarefa se necessário. Descrever os estados e os erros antes de escrever código.
5. **Localizações:** código próprio do site em `site/extensions/<id>/`, aparência em `site/themes/<id>/`, dados sob `$ctx['data']`, conteúdos e definições através da administração ou do MCP. Nunca editar `app/`, `assets/`, `index.php` nem o updater.
6. **Contrato atual:** Uma parte depende de um ponto de extensão ausente do contrato 2.0 (tipos de conteúdo, contribuição SEO ou JSON-LD, política de conteúdo por funcionalidade, filtro de renderização). Entregar a parte nativa e documentar com precisão a lacuna, sem soluções de contorno.
7. **Invariante de segurança:** Nenhuma chave de API no código, no repositório ou numa página pública. Verificar também as permissões do lado do servidor, o escape com `e()`, a validação dos dados e a ausência de segredos ou de dados pessoais no HTML público ou numa cache partilhada.
8. **Provas:** escrever o teste positivo «Inscrever um endereço de teste e reencontrá-lo no serviço» e o teste de recusa «Uma chave revogada produz um erro registado, não uma fuga». Medir as regressões de SEO e de desempenho, documentar a reversão.
9. **Validação nativa:** `php tools/validate.php <dossier> --json`, `php tests/run.php` e `php tools/measure.php --check` num checkout oficial para qualquer pacote produzido. Para uma parte não suportada pelo núcleo, fornecer uma nota de lacuna e um teste bloqueante, nunca um êxito fictício.

## Entregáveis obrigatórios
- Miniespecificação: objetivo, utilizadores, percursos, estados, dados, medições.
- Matriz de autorizações e de cache: rota, método, sessão, visibilidade, indexação.
- Pacote ou definições para a parte nativa, e nota de lacuna precisa para a parte bloqueada.
- Testes dos casos positivos e das recusas, procedimento de desativação que conserva os dados, nota de compatibilidade.

## Critérios de aceitação
- Inscrever um endereço de teste e reencontrá-lo no serviço.
- Uma chave revogada produz um erro registado, não uma fuga.
- Nada é publicado, ativado nem colocado em produção sem uma pessoa autorizada; não é prometida nenhuma pontuação, classificação ou citação por uma IA.
- As partes não suportadas pelo Éclair 2.0 são explicitamente assinaladas como **não entregáveis em produção**.

**Estado de maturidade deste skill:** `partly-blocked-by-core-contract`. Ver `references/acceptance.md` para os casos de ensaio reproduzíveis.
