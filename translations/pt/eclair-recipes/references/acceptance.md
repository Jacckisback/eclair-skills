# Plano de validação — Receitas

## Modelo de dados
Receita, ingredientes, passos, tempo, porções.

## Implementação esperada
Estruturar cada receita em ingredientes e passos, acrescentar tempo e porções, prever uma versão imprimível.

## Testes a prever
1. Nominal: Seguir uma receita publicada em dispositivo móvel e imprimi-la.
2. Controlo de recusa: Uma receita sem quantidades não é publicada.
3. Invariante: Nenhuma alegação de saúde não fundamentada.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
