# Plano de validação — Ligações de pagamento

## Modelo de dados
Produto ou variante, ligação de pagamento, prestador.

## Implementação esperada
Criar a ligação junto do prestador, colá-la na ficha ou na variante, testar em modo de teste, verificar o recibo e o reembolso do lado do prestador.

## Testes a prever
1. Nominal: Comprar em modo de teste e verificar o montante e o recibo.
2. Controlo de recusa: Uma ligação para um domínio não reconhecido é recusada.
3. Invariante: Nenhum dado bancário no site; uma ligação só conduz ao domínio do prestador.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
