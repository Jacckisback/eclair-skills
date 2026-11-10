# Plano de validação — Assistência e tickets

## Modelo de dados
Ticket, requerente, estado, trocas de mensagens, prioridade.

## Implementação esperada
Começar por formulário de contacto e caixa de entrada; conceber estados, prazos e área de acompanhamento para mais tarde.

## Testes a prever
1. Nominal: Percorrer um pedido da abertura ao encerramento.
2. Controlo de recusa: Um ticket não pode ser lido adivinhando o seu número.
3. Invariante: Um requerente só vê os seus próprios tickets.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
