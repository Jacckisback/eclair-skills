# Plano de validação — Filtros e ordenação do catálogo

## Modelo de dados
Critério, valor, combinação, endereço filtrado.

## Implementação esperada
Apoiar-se nos filtros por categoria nativos; adicionar filtros do lado do navegador sobre dados públicos, com endereços canónicos controlados.

## Testes a prever
1. Nominal: Filtrar e ordenar um catálogo de teste em dispositivo móvel.
2. Controlo de recusa: Uma combinação sem resultados apresenta uma mensagem, não uma página vazia indexável.
3. Invariante: As combinações de filtros não criam uma infinidade de páginas indexáveis.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
