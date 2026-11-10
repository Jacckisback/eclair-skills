# Plano de validação — Tarefas agendadas

## Modelo de dados
Tarefa, frequência, última execução, resultado.

## Implementação esperada
Declarar a tarefa no manifesto (no máximo uma vez por hora), chamar o endereço secreto do núcleo a partir do agendador do fornecedor de alojamento, registar.

## Testes a prever
1. Nominal: Executar a tarefa duas vezes seguidas e verificar um único efeito.
2. Controlo de recusa: Uma chamada sem o token secreto não desencadeia nada.
3. Invariante: O endereço secreto das tarefas nunca é publicado; cada tarefa é idempotente.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
