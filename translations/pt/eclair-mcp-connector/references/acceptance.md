# Plano de validação — Conector MCP

## Modelo de dados
Cliente autorizado, token, ferramentas disponíveis, rascunhos criados.

## Implementação esperada
Fazer ativar o conector pelo proprietário, autorizar o cliente, trabalhar em rascunhos e propostas, saber cortar o acesso.

## Testes a prever
1. Nominal: Criar um rascunho através do conector e depois revogar o acesso.
2. Controlo de recusa: Após a revogação, qualquer pedido do cliente é recusado.
3. Invariante: O conector não publica nem elimina; o acesso é revogável a qualquer momento.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
