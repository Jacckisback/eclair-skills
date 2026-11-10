# Plano de validação — Encomendas e pagamentos

## Modelo de dados
Encomenda, tentativa de pagamento, identificador do fornecedor, prova de webhook, idempotency key, reembolso.

## Implementação esperada
Detalhar as transições autorizadas; armazenar a prova da notificação e a respetiva data e hora; tratar o webhook de forma durável; prever reconciliation e reembolso parcial.

## Testes a prever
1. Nominal: Testar webhook invertido, fora de ordem, reemitido e pagamento recusado.
2. Controlo de recusa: Um webhook sem assinatura válida não modifica nem a encomenda nem o acesso LMS.
3. Invariante: Nunca armazenar dados brutos de cartão bancário; checkout alojado no prestador e assinatura dos webhooks verificada.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
