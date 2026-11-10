---
name: eclair-privacy-analytics
description: "Medir a audiência sem cookies nem criação de perfis. Use on Éclair CMS 2.x when the user wants to: medir a audiência sem cookies nem definição de perfis. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Medição de audiência respeitadora da privacidade — Éclair CMS 2.x

## Desencadeador e resultado esperado
Utilizar este skill para **medir a audiência sem cookies nem definição de perfis**. Esta funcionalidade está **em parte bloqueada pelo contrato do núcleo**: o skill entrega o que é nativo e documenta a lacuna. Este skill é um **workflow de agente**, não uma extensão PHP funcional nem uma garantia de conformidade.

**Equivalente WordPress:** Matomo, Plausible, Koko Analytics. Família: Marketing e audiência.

## Diagnóstico obrigatório antes de qualquer modificação
1. Ler `references/core-map.md` (o que o núcleo já faz) e `references/native-contract.md`; verificar a versão real do CMS e as capacidades em `GET /<admin>/api/capabilities` (se o acesso for autorizado).
2. Ler `references/family-contract.md` e `references/acceptance.md`. Nunca copiar o antigo sistema de packs v0.x nem código PHP do WordPress para o Éclair 2.
3. Identificar o modelo de dados: **Página vista, origem, período, agregados**. Documentar o que é público, o que é privado e de onde vem cada dado.

## Procedimento específico
4. **Percurso:** Preferir os registos do servidor ou uma ferramenta sem cookies em alojamento próprio; um script de terceiros depende da política de conteúdo nativa. Descrever os estados e os erros antes de escrever código.
5. **Localizações:** código próprio do site em `site/extensions/<id>/`, aparência em `site/themes/<id>/`, dados sob `$ctx['data']`, conteúdos e definições através da administração ou do MCP. Nunca editar `app/`, `assets/`, `index.php` nem o updater.
6. **Contrato atual:** Uma parte depende de um ponto de extensão ausente do contrato 2.0 (tipos de conteúdo, contribuição SEO ou JSON-LD, política de conteúdo por funcionalidade, filtro de renderização). Entregar a parte nativa e documentar com precisão a lacuna, sem soluções de contorno.
7. **Invariante de segurança:** Nenhum endereço IP completo nem identificador de visitante é conservado. Verificar também as permissões do lado do servidor, o escape com `e()`, a validação dos dados e a ausência de segredos ou de dados pessoais no HTML público ou numa cache partilhada.
8. **Provas:** escrever o teste positivo «Comparar as páginas vistas medidas com um percurso de teste» e o teste de recusa «Nenhum cookie é depositado pela medição». Medir as regressões de SEO e de desempenho, documentar a reversão.
9. **Validação nativa:** `php tools/validate.php <dossier> --json`, `php tests/run.php` e `php tools/measure.php --check` num checkout oficial para qualquer pacote produzido. Para uma parte não suportada pelo núcleo, fornecer uma nota de lacuna e um teste bloqueante, nunca um êxito fictício.

## Entregáveis obrigatórios
- Miniespecificação: objetivo, utilizadores, percursos, estados, dados, medições.
- Matriz de autorizações e de cache: rota, método, sessão, visibilidade, indexação.
- Pacote ou definições para a parte nativa, e nota de lacuna precisa para a parte bloqueada.
- Testes dos casos positivos e das recusas, procedimento de desativação que conserva os dados, nota de compatibilidade.

## Critérios de aceitação
- Comparar as páginas vistas medidas com um percurso de teste.
- Nenhum cookie é depositado pela medição.
- Nada é publicado, ativado nem colocado em produção sem uma pessoa autorizada; não é prometida nenhuma pontuação, classificação ou citação por uma IA.
- As partes não suportadas pelo Éclair 2.0 são explicitamente assinaladas como **não entregáveis em produção**.

**Estado de maturidade deste skill:** `partly-blocked-by-core-contract`. Ver `references/acceptance.md` para os casos de ensaio reproduzíveis.
