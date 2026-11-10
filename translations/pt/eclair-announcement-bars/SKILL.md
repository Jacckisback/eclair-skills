---
name: eclair-announcement-bars
description: "Mostrar uma barra de anúncio temporária. Use on Éclair CMS 2.x when the user wants to: apresentar uma faixa de informação temporária. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Faixas de anúncio — Éclair CMS 2.x

## Desencadeador e resultado esperado
Utilizar este skill para **apresentar uma faixa de informação temporária**. Esta funcionalidade é **realizável hoje** com o contrato nativo (tema, blocos, rotas GET, páginas de administração, tarefas). Este skill é um **workflow de agente**, não uma extensão PHP funcional nem uma garantia de conformidade.

**Equivalente WordPress:** Hello Bar, faixas de notificação. Família: Marketing e audiência.

## Diagnóstico obrigatório antes de qualquer modificação
1. Ler `references/core-map.md` (o que o núcleo já faz) e `references/native-contract.md`; verificar a versão real do CMS e as capacidades em `GET /<admin>/api/capabilities` (se o acesso for autorizado).
2. Ler `references/family-contract.md` e `references/acceptance.md`. Nunca copiar o antigo sistema de packs v0.x nem código PHP do WordPress para o Éclair 2.
3. Identificar o modelo de dados: **Mensagem, ligação, datas de início e de fim**. Documentar o que é público, o que é privado e de onde vem cada dado.

## Procedimento específico
4. **Percurso:** Renderizar a faixa do lado do servidor com datas de validade, sem deslocamento da disposição, retirada automaticamente no termo do prazo. Descrever os estados e os erros antes de escrever código.
5. **Localizações:** código próprio do site em `site/extensions/<id>/`, aparência em `site/themes/<id>/`, dados sob `$ctx['data']`, conteúdos e definições através da administração ou do MCP. Nunca editar `app/`, `assets/`, `index.php` nem o updater.
6. **Contrato atual:** Realizável com `eclair-extension/1` e o contrato de tema: rotas GET públicas colocáveis em cache, páginas de administração protegidas, blocos e definições declarativos, tarefas agendadas, recursos. Verificar primeiro se um bloco ou uma definição nativa não é suficiente.
7. **Invariante de segurança:** Nenhum anúncio expirado continua a ser servido pela cache. Verificar também as permissões do lado do servidor, o escape com `e()`, a validação dos dados e a ausência de segredos ou de dados pessoais no HTML público ou numa cache partilhada.
8. **Provas:** escrever o teste positivo «Apresentar, fechar e deixar expirar uma faixa» e o teste de recusa «Após a data de fim, a faixa já não aparece em nenhuma página». Medir as regressões de SEO e de desempenho, documentar a reversão.
9. **Validação nativa:** `php tools/validate.php <dossier> --json`, `php tests/run.php` e `php tools/measure.php --check` num checkout oficial para qualquer pacote produzido. Para uma parte não suportada pelo núcleo, fornecer uma nota de lacuna e um teste bloqueante, nunca um êxito fictício.

## Entregáveis obrigatórios
- Miniespecificação: objetivo, utilizadores, percursos, estados, dados, medições.
- Matriz de autorizações e de cache: rota, método, sessão, visibilidade, indexação.
- Pacote `extension.json`/`extension.php` ou pacote de tema validado, apenas se um bloco ou uma definição nativa não for suficiente.
- Testes dos casos positivos e das recusas, procedimento de desativação que conserva os dados, nota de compatibilidade.

## Critérios de aceitação
- Apresentar, fechar e deixar expirar uma faixa.
- Após a data de fim, a faixa já não aparece em nenhuma página.
- Nada é publicado, ativado nem colocado em produção sem uma pessoa autorizada; não é prometida nenhuma pontuação, classificação ou citação por uma IA.
- As partes não suportadas pelo Éclair 2.0 são explicitamente assinaladas como **não entregáveis em produção**.

**Estado de maturidade deste skill:** `native-v2-workflow`. Ver `references/acceptance.md` para os casos de ensaio reproduzíveis.
