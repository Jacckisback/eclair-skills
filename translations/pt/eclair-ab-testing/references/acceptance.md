# Plano de validação — Testes A/B

## Modelo de dados
Variante, repartição, objetivo, resultado.

## Implementação esperada
Testar por períodos sucessivos ou por endereços distintos, em vez de variantes na cache; fixar antecipadamente a hipótese, a duração e a medição.

## Testes a prever
1. Nominal: Realizar um teste em duas páginas de destino distintas.
2. Controlo de recusa: Um resultado sem volume suficiente não é apresentado como conclusivo.
3. Invariante: Nenhuma variante é armazenada na cache partilhada em função do visitante.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
