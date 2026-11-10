# Plano de validação — Workflows de IA

## Modelo de dados
Rascunho, proposta, validação, modelo, custo, fonte e auditoria.

## Implementação esperada
Utilizar as capacidades MCP do núcleo, manter um humano no circuito, limitar acesso e orçamento; avaliar qualidade e alucinações.

## Testes a prever
1. Nominal: Testar prompt injection, mudança de contexto e rollback.
2. Controlo de recusa: Uma instrução hostil num artigo importado não se torna um comando executado.
3. Invariante: Nenhuma IA publica, implementa, elimina ou modifica PHP diretamente por MCP sem controlo.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
