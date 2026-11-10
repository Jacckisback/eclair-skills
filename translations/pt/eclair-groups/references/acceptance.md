# Plano de validação — Grupos

## Modelo de dados
Grupo, visibilidade, membros, papéis.

## Implementação esperada
Definir criação, adesão, papéis e visibilidade; aplicar os direitos em cada leitura.

## Testes a prever
1. Nominal: Simular criação, pedido de adesão e exclusão.
2. Controlo de recusa: Um não-membro não lê nenhum conteúdo de um grupo privado.
3. Invariante: O conteúdo de um grupo privado não aparece nem na pesquisa nem na cache pública.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
