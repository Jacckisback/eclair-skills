---
name: eclair-maintenance-mode
description: "Mostrar uma página de manutenção limpa durante os trabalhos. Use on Éclair CMS 2.x when the user wants to: apresentar uma página de manutenção cuidada durante os trabalhos. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Modo de manutenção — Éclair CMS 2.x

## Desencadeador e resultado esperado
Utilizar este skill para **apresentar uma página de manutenção cuidada durante os trabalhos**. Esta funcionalidade é **realizável hoje** com o contrato nativo (tema, blocos, rotas GET, páginas de administração, tarefas). Este skill é um **workflow de agente**, não uma extensão PHP funcional nem uma garantia de conformidade.

**Equivalente WordPress:** WP Maintenance Mode, SeedProd. Família: Administração e manutenção.

## Diagnóstico obrigatório antes de qualquer modificação
1. Ler `references/core-map.md` (o que o núcleo já faz) e `references/native-contract.md`; verificar a versão real do CMS e as capacidades em `GET /<admin>/api/capabilities` (se o acesso for autorizado).
2. Ler `references/family-contract.md` e `references/acceptance.md`. Nunca copiar o antigo sistema de packs v0.x nem código PHP do WordPress para o Éclair 2.
3. Identificar o modelo de dados: **Estado de manutenção, mensagem, duração prevista, acesso da equipa**. Documentar o que é público, o que é privado e de onde vem cada dado.

## Procedimento específico
4. **Percurso:** Servir uma página estática com o estado HTTP temporário correto ao nível do servidor, manter o acesso à administração, prever o regresso online. Descrever os estados e os erros antes de escrever código.
5. **Localizações:** código próprio do site em `site/extensions/<id>/`, aparência em `site/themes/<id>/`, dados sob `$ctx['data']`, conteúdos e definições através da administração ou do MCP. Nunca editar `app/`, `assets/`, `index.php` nem o updater.
6. **Contrato atual:** Realizável com `eclair-extension/1` e o contrato de tema: rotas GET públicas colocáveis em cache, páginas de administração protegidas, blocos e definições declarativos, tarefas agendadas, recursos. Verificar primeiro se um bloco ou uma definição nativa não é suficiente.
7. **Invariante de segurança:** A página de manutenção não revela nem a versão nem o caminho do servidor. Verificar também as permissões do lado do servidor, o escape com `e()`, a validação dos dados e a ausência de segredos ou de dados pessoais no HTML público ou numa cache partilhada.
8. **Provas:** escrever o teste positivo «Ativar, verificar estado 503 e cabeçalho de nova tentativa, desativar» e o teste de recusa «Os robôs nunca recebem a página de manutenção com um estado 200». Medir as regressões de SEO e de desempenho, documentar a reversão.
9. **Validação nativa:** `php tools/validate.php <dossier> --json`, `php tests/run.php` e `php tools/measure.php --check` num checkout oficial para qualquer pacote produzido. Para uma parte não suportada pelo núcleo, fornecer uma nota de lacuna e um teste bloqueante, nunca um êxito fictício.

## Entregáveis obrigatórios
- Miniespecificação: objetivo, utilizadores, percursos, estados, dados, medições.
- Matriz de autorizações e de cache: rota, método, sessão, visibilidade, indexação.
- Pacote `extension.json`/`extension.php` ou pacote de tema validado, apenas se um bloco ou uma definição nativa não for suficiente.
- Testes dos casos positivos e das recusas, procedimento de desativação que conserva os dados, nota de compatibilidade.

## Critérios de aceitação
- Ativar, verificar estado 503 e cabeçalho de nova tentativa, desativar.
- Os robôs nunca recebem a página de manutenção com um estado 200.
- Nada é publicado, ativado nem colocado em produção sem uma pessoa autorizada; não é prometida nenhuma pontuação, classificação ou citação por uma IA.
- As partes não suportadas pelo Éclair 2.0 são explicitamente assinaladas como **não entregáveis em produção**.

**Estado de maturidade deste skill:** `native-v2-workflow`. Ver `references/acceptance.md` para os casos de ensaio reproduzíveis.
