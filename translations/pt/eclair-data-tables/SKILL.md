---
name: eclair-data-tables
description: "Apresentar tabelas legíveis em dispositivos móveis. Use on Éclair CMS 2.x when the user wants to: apresentar tabelas legíveis em dispositivos móveis. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Tabelas de dados — Éclair CMS 2.x

## Desencadeador e resultado esperado
Utilizar este skill para **apresentar tabelas legíveis em dispositivos móveis**. Esta funcionalidade está **já integrada no núcleo Éclair 2.0**: o skill orienta a sua configuração e a sua verificação, sem escrever nenhuma extensão. Este skill é um **workflow de agente**, não uma extensão PHP funcional nem uma garantia de conformidade.

**Equivalente WordPress:** TablePress, wpDataTables. Família: Blocos e componentes.

## Diagnóstico obrigatório antes de qualquer modificação
1. Ler `references/core-map.md` (o que o núcleo já faz) e `references/native-contract.md`; verificar a versão real do CMS e as capacidades em `GET /<admin>/api/capabilities` (se o acesso for autorizado).
2. Ler `references/family-contract.md` e `references/acceptance.md`. Nunca copiar o antigo sistema de packs v0.x nem código PHP do WordPress para o Éclair 2.
3. Identificar o modelo de dados: **Tabela, cabeçalhos, linhas, legenda**. Documentar o que é público, o que é privado e de onde vem cada dado.

## Procedimento específico
4. **Percurso:** Utilizar o bloco de tabela nativo, adicionar legenda e cabeçalhos, prever um deslocamento horizontal controlado. Descrever os estados e os erros antes de escrever código.
5. **Localizações:** código próprio do site em `site/extensions/<id>/`, aparência em `site/themes/<id>/`, dados sob `$ctx['data']`, conteúdos e definições através da administração ou do MCP. Nunca editar `app/`, `assets/`, `index.php` nem o updater.
6. **Contrato atual:** A funcionalidade existe no núcleo: configurá-la através da administração ou, em rascunho, através do conector MCP. Não a duplicar numa extensão e nunca modificar o núcleo para a adaptar; se uma necessidade ultrapassar o que o núcleo oferece, assinalá-la como uma lacuna.
7. **Invariante de segurança:** Nenhum dado pessoal numa tabela pública sem consentimento. Verificar também as permissões do lado do servidor, o escape com `e()`, a validação dos dados e a ausência de segredos ou de dados pessoais no HTML público ou numa cache partilhada.
8. **Provas:** escrever o teste positivo «Ler a tabela num dispositivo móvel e com o leitor de ecrã» e o teste de recusa «Uma tabela larga não provoca o deslocamento horizontal de toda a página». Medir as regressões de SEO e de desempenho, documentar a reversão.
9. **Validação nativa:** `php tools/validate.php <dossier> --json`, `php tests/run.php` e `php tools/measure.php --check` num checkout oficial para qualquer pacote produzido. Para uma parte não suportada pelo núcleo, fornecer uma nota de lacuna e um teste bloqueante, nunca um êxito fictício.

## Entregáveis obrigatórios
- Miniespecificação: objetivo, utilizadores, percursos, estados, dados, medições.
- Matriz de autorizações e de cache: rota, método, sessão, visibilidade, indexação.
- Definições e conteúdos preparados através da administração ou em rascunho através do MCP; **nenhuma extensão** enquanto o nativo for suficiente.
- Testes dos casos positivos e das recusas, procedimento de desativação que conserva os dados, nota de compatibilidade.

## Critérios de aceitação
- Ler a tabela num dispositivo móvel e com o leitor de ecrã.
- Uma tabela larga não provoca o deslocamento horizontal de toda a página.
- Nada é publicado, ativado nem colocado em produção sem uma pessoa autorizada; não é prometida nenhuma pontuação, classificação ou citação por uma IA.
- As partes não suportadas pelo Éclair 2.0 são explicitamente assinaladas como **não entregáveis em produção**.

**Estado de maturidade deste skill:** `core-builtin-configuration-workflow`. Ver `references/acceptance.md` para os casos de ensaio reproduzíveis.
