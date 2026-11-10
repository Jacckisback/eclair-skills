# Plano de validação — Promoções e cupões

## Modelo de dados
Código, orçamento, datas, quota, condições de carrinho, utilizações e exclusões.

## Implementação esperada
Definir a ordem de cálculo e o arredondamento; verificar o cupão antes da encomenda; contabilizar as utilizações de forma atómica; rastrear o cancelamento e a devolução.

## Testes a prever
1. Nominal: Testar cupões expirados, esgotados, limiar e exclusões.
2. Controlo de recusa: Duas encomendas simultâneas não podem consumir o último cupão único.
3. Invariante: A decisão de elegibilidade provém dos dados do servidor e não do desconto introduzido em HTML.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
