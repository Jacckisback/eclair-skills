---
name: eclair-structured-data
description: "Adicionar ou verificar dados schema.org coerentes com o conteúdo. Use on Éclair CMS 2.x when the user wants to: adicionar ou verificar schema.org coerente com o conteúdo. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Dados estruturados — Éclair CMS 2.x

## Desencadeador e resultado esperado
Utilizar este skill para **adicionar ou verificar schema.org coerente com o conteúdo**. Esta funcionalidade está **em parte bloqueada pelo contrato do núcleo**: o skill entrega o que é nativo e documenta a lacuna. Este skill é um **workflow de agente**, não uma extensão PHP funcional nem uma garantia de conformidade.

**Equivalente WordPress:** Schema Pro, Rank Math Schema. Família: SEO, GEO e migração.

## Diagnóstico obrigatório antes de qualquer modificação
1. Ler `references/core-map.md` (o que o núcleo já faz) e `references/native-contract.md`; verificar a versão real do CMS e as capacidades em `GET /<admin>/api/capabilities` (se o acesso for autorizado).
2. Ler `references/family-contract.md` e `references/acceptance.md`. Nunca copiar o antigo sistema de packs v0.x nem código PHP do WordPress para o Éclair 2.
3. Identificar o modelo de dados: **WebPage, Article, Product, FAQ pertinente, Organization, BreadcrumbList**. Documentar o que é público, o que é privado e de onde vem cada dado.

## Procedimento específico
4. **Percurso:** Inspecionar o JSON-LD nativo antes de adicionar um tipo; evitar duplicação; alinhar cada campo com os dados visíveis e as diretrizes dos motores de pesquisa. Descrever os estados e os erros antes de escrever código.
5. **Localizações:** código próprio do site em `site/extensions/<id>/`, aparência em `site/themes/<id>/`, dados sob `$ctx['data']`, conteúdos e definições através da administração ou do MCP. Nunca editar `app/`, `assets/`, `index.php` nem o updater.
6. **Contrato atual:** O SEO/GEO de base é nativo. As extensões ainda não dispõem de uma API universal para injetar o JSON-LD; documentar a lacuna do contrato em vez de remendar o HTML ou scripts.
7. **Invariante de segurança:** O Éclair v2 ainda não expõe todas as contribuições JSON-LD às extensões; propor uma RFC em vez de uma injeção opaca. Verificar também as permissões do lado do servidor, o escape com `e()`, a validação dos dados e a ausência de segredos ou de dados pessoais no HTML público ou numa cache partilhada.
8. **Provas:** escrever o teste positivo «Testar JSON válido, canonical, identificadores e conteúdo apresentado» e o teste de recusa «Nenhum preço/avaliação/product inventado ou ausente da página figura no JSON-LD». Medir as regressões de SEO e de desempenho, documentar a reversão.
9. **Validação nativa:** `php tools/validate.php <dossier> --json`, `php tests/run.php` e `php tools/measure.php --check` num checkout oficial para qualquer pacote produzido. Para uma parte não suportada pelo núcleo, fornecer uma nota de lacuna e um teste bloqueante, nunca um êxito fictício.

## Entregáveis obrigatórios
- Miniespecificação: objetivo, utilizadores, percursos, estados, dados, medições.
- Matriz de autorizações e de cache: rota, método, sessão, visibilidade, indexação.
- Pacote ou definições para a parte nativa, e nota de lacuna precisa para a parte bloqueada.
- Testes dos casos positivos e das recusas, procedimento de desativação que conserva os dados, nota de compatibilidade.

## Critérios de aceitação
- Testar JSON válido, canonical, identificadores e conteúdo apresentado.
- Nenhum preço/avaliação/product inventado ou ausente da página figura no JSON-LD.
- Nada é publicado, ativado nem colocado em produção sem uma pessoa autorizada; não é prometida nenhuma pontuação, classificação ou citação por uma IA.
- As partes não suportadas pelo Éclair 2.0 são explicitamente assinaladas como **não entregáveis em produção**.

**Estado de maturidade deste skill:** `partly-blocked-by-core-contract`. Ver `references/acceptance.md` para os casos de ensaio reproduzíveis.
