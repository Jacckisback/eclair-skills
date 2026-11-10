# Plano de validação — IVA e faturação

## Modelo de dados
País de venda e de entrega, localização fiscal, taxa em vigor, fatura, nota de crédito, sequência.

## Implementação esperada
Listar as jurisdições e os tipos de clientes; consultar as regras atualizadas e aconselhamento contabilístico; fixar a base tributável/taxa no momento da encomenda; preparar exportações de faturas e notas de crédito.

## Testes a prever
1. Nominal: Testar venda doméstica, transfronteiriça, reembolso e alteração de taxa.
2. Controlo de recusa: Uma fatura emitida e depois anulada não deve ser apagada nem renumerada silenciosamente.
3. Invariante: Nunca aplicar uma taxa de IVA universal nem pretender garantir a conformidade fiscal sem validação local.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
