---
name: eclair-multilingual-seo
description: "Gerir várias línguas sem duplicados nem canonical erradas (hreflang). Use on Éclair CMS 2.x when the user wants to: gerir várias línguas sem duplicação nem canonical incorretas. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# SEO multilingue — Éclair CMS 2.x

## Desencadeador e resultado esperado
Utilizar este skill para **gerir várias línguas sem duplicação nem canonical incorretas**. Esta funcionalidade é **realizável hoje** com o contrato nativo (tema, blocos, rotas GET, páginas de administração, tarefas). Este skill é um **workflow de agente**, não uma extensão PHP funcional nem uma garantia de conformidade.

**Equivalente WordPress:** WPML SEO, Polylang. Família: SEO, GEO e migração.

## Diagnóstico obrigatório antes de qualquer modificação
1. Ler `references/core-map.md` (o que o núcleo já faz) e `references/native-contract.md`; verificar a versão real do CMS e as capacidades em `GET /<admin>/api/capabilities` (se o acesso for autorizado).
2. Ler `references/family-contract.md` e `references/acceptance.md`. Nunca copiar o antigo sistema de packs v0.x nem código PHP do WordPress para o Éclair 2.
3. Identificar o modelo de dados: **Língua, URL de tradução, hreflang recíproco, título e sitemap**. Documentar o que é público, o que é privado e de onde vem cada dado.

## Procedimento específico
4. **Percurso:** Inventariar as línguas publicadas, definir o mapping das traduções, testar canonical por língua, hreflang/x-default e ausência de redirecionamento intrusivo. Descrever os estados e os erros antes de escrever código.
5. **Localizações:** código próprio do site em `site/extensions/<id>/`, aparência em `site/themes/<id>/`, dados sob `$ctx['data']`, conteúdos e definições através da administração ou do MCP. Nunca editar `app/`, `assets/`, `index.php` nem o updater.
6. **Contrato atual:** O SEO/GEO de base é nativo. As extensões ainda não dispõem de uma API universal para injetar o JSON-LD; documentar a lacuna do contrato em vez de remendar o HTML ou scripts.
7. **Invariante de segurança:** Não utilizar uma tradução automática não verificada como página definitiva. Verificar também as permissões do lado do servidor, o escape com `e()`, a validação dos dados e a ausência de segredos ou de dados pessoais no HTML público ou numa cache partilhada.
8. **Provas:** escrever o teste positivo «Testar pares FR/ES/EN, páginas em falta e mudança de língua» e o teste de recusa «Cada ligação hreflang aponta para um URL 200 indexável e recíproco». Medir as regressões de SEO e de desempenho, documentar a reversão.
9. **Validação nativa:** `php tools/validate.php <dossier> --json`, `php tests/run.php` e `php tools/measure.php --check` num checkout oficial para qualquer pacote produzido. Para uma parte não suportada pelo núcleo, fornecer uma nota de lacuna e um teste bloqueante, nunca um êxito fictício.

## Entregáveis obrigatórios
- Miniespecificação: objetivo, utilizadores, percursos, estados, dados, medições.
- Matriz de autorizações e de cache: rota, método, sessão, visibilidade, indexação.
- Pacote `extension.json`/`extension.php` ou pacote de tema validado, apenas se um bloco ou uma definição nativa não for suficiente.
- Testes dos casos positivos e das recusas, procedimento de desativação que conserva os dados, nota de compatibilidade.

## Critérios de aceitação
- Testar pares FR/ES/EN, páginas em falta e mudança de língua.
- Cada ligação hreflang aponta para um URL 200 indexável e recíproco.
- Nada é publicado, ativado nem colocado em produção sem uma pessoa autorizada; não é prometida nenhuma pontuação, classificação ou citação por uma IA.
- As partes não suportadas pelo Éclair 2.0 são explicitamente assinaladas como **não entregáveis em produção**.

**Estado de maturidade deste skill:** `native-v2-workflow`. Ver `references/acceptance.md` para os casos de ensaio reproduzíveis.
