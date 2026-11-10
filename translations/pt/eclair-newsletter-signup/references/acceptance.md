# Plano de validação — Subscrição da newsletter

## Modelo de dados
Endereço de e-mail, consentimento, data, origem.

## Implementação esperada
Utilizar uma página de subscrição alojada pelo serviço de e-mailing ou uma ligação, enquanto o próprio site não puder receber subscrições; dupla confirmação.

## Testes a prever
1. Nominal: Subscrever, confirmar, cancelar a subscrição.
2. Controlo de recusa: Uma subscrição não confirmada não recebe nenhum envio.
3. Invariante: Nenhum endereço é adicionado a uma lista sem consentimento explícito e prova.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
