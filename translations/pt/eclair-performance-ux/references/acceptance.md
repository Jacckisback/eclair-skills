# Plano de validação — Desempenho UX

## Modelo de dados
LCP, CLS, INP, peso dos assets, CSS, JS, cache e tipos de letra.

## Implementação esperada
Medir antes/depois através de tools/measure.php --check, do Chrome Lighthouse e de uma rede lenta, otimizar imagens e scripts.

## Testes a prever
1. Nominal: Testar o site público sem extensão, com extensão e em dispositivos móveis.
2. Controlo de recusa: Uma melhoria declarada é acompanhada de medições reprodutíveis antes/depois.
3. Invariante: Não degradar o caminho de cache PHP nem desativar a CSP por comodidade.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
