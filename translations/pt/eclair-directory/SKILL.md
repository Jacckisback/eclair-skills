---
name: eclair-directory
description: "Criar fichas e filtros indexáveis de um diretório profissional. Use on Éclair CMS 2.x when the user wants to: criar fichas e filtros indexáveis. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Diretório profissional — Éclair CMS 2.x

## Desencadeador e resultado esperado
Utilizar este skill para **criar fichas e filtros indexáveis**. A **parte pública em leitura é realizável hoje**; as escritas por visitantes exigem mais do que o contrato atual. Este skill é um **workflow de agente**, não uma extensão PHP funcional nem uma garantia de conformidade.

**Equivalente WordPress:** GeoDirectory, Business Directory Plugin. Família: Aplicações de negócio.

## Diagnóstico obrigatório antes de qualquer modificação
1. Ler `references/core-map.md` (o que o núcleo já faz) e `references/native-contract.md`; verificar a versão real do CMS e as capacidades em `GET /<admin>/api/capabilities` (se o acesso for autorizado).
2. Ler `references/family-contract.md` e `references/acceptance.md`. Nunca copiar o antigo sistema de packs v0.x nem código PHP do WordPress para o Éclair 2.
3. Identificar o modelo de dados: **Ficha, categoria, localização, contacto público, estado de verificação**. Documentar o que é público, o que é privado e de onde vem cada dado.

## Procedimento específico
4. **Percurso:** Separar dados profissionais públicos e privados; criar páginas de categoria, canonical, moderação e filtros limitados. Descrever os estados e os erros antes de escrever código.
5. **Localizações:** código próprio do site em `site/extensions/<id>/`, aparência em `site/themes/<id>/`, dados sob `$ctx['data']`, conteúdos e definições através da administração ou do MCP. Nunca editar `app/`, `assets/`, `index.php` nem o updater.
6. **Contrato atual:** As montras públicas são possíveis com GET; reservas, pagamentos, candidaturas, CRM e dados pessoais exigem POST seguro, armazenamento adequado e permissões verificadas do lado do servidor.
7. **Invariante de segurança:** Não publicar morada pessoal, telefone ou contactos sensíveis sem autorização. Verificar também as permissões do lado do servidor, o escape com `e()`, a validação dos dados e a ausência de segredos ou de dados pessoais no HTML público ou numa cache partilhada.
8. **Provas:** escrever o teste positivo «Testar fichas falsas, duplicados, eliminação e pesquisa vazia» e o teste de recusa «Uma ficha pendente não aparece nem no sitemap nem nos dados estruturados». Medir as regressões de SEO e de desempenho, documentar a reversão.
9. **Validação nativa:** `php tools/validate.php <dossier> --json`, `php tests/run.php` e `php tools/measure.php --check` num checkout oficial para qualquer pacote produzido. Para uma parte não suportada pelo núcleo, fornecer uma nota de lacuna e um teste bloqueante, nunca um êxito fictício.

## Entregáveis obrigatórios
- Miniespecificação: objetivo, utilizadores, percursos, estados, dados, medições.
- Matriz de autorizações e de cache: rota, método, sessão, visibilidade, indexação.
- Pacote só de leitura (rotas GET) validado, e plano escrito para a parte de escrita, claramente marcada como não entregue.
- Testes dos casos positivos e das recusas, procedimento de desativação que conserva os dados, nota de compatibilidade.

## Critérios de aceitação
- Testar fichas falsas, duplicados, eliminação e pesquisa vazia.
- Uma ficha pendente não aparece nem no sitemap nem nos dados estruturados.
- Nada é publicado, ativado nem colocado em produção sem uma pessoa autorizada; não é prometida nenhuma pontuação, classificação ou citação por uma IA.
- As partes não suportadas pelo Éclair 2.0 são explicitamente assinaladas como **não entregáveis em produção**.

**Estado de maturidade deste skill:** `public-read-only-prototype-possible`. Ver `references/acceptance.md` para os casos de ensaio reproduzíveis.
