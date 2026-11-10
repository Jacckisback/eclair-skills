# Plano de validação — Subscrições e adesões

## Modelo de dados
Plano, adesão, renovação, período, rescisão, pagamento, direito.

## Implementação esperada
Calcular direitos a partir do estado verificado, prever mudanças de plano e períodos de tolerância, tratar eventos de faturação de forma idempotente.

## Testes a prever
1. Nominal: Testar falha de débito, pro rata, reembolso e rescisão.
2. Controlo de recusa: Dois eventos idênticos não prolongam a subscrição duas vezes.
3. Invariante: Um recibo do navegador nunca é suficiente para renovar um acesso pago.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
