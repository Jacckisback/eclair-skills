# Plano de validação — Tabelas de dados

## Modelo de dados
Tabela, cabeçalhos, linhas, legenda.

## Implementação esperada
Utilizar o bloco de tabela nativo, adicionar legenda e cabeçalhos, prever um deslocamento horizontal controlado.

## Testes a prever
1. Nominal: Ler a tabela num dispositivo móvel e com o leitor de ecrã.
2. Controlo de recusa: Uma tabela larga não provoca o deslocamento horizontal de toda a página.
3. Invariante: Nenhum dado pessoal numa tabela pública sem consentimento.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
