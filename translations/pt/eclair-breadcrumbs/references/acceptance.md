# Plano de validação — Trilho de navegação

## Modelo de dados
Níveis, rótulos, endereços.

## Implementação esperada
Verificar a coerência entre a estrutura em árvore, o trilho de navegação apresentado e os dados estruturados do núcleo.

## Testes a prever
1. Nominal: Comparar o trilho apresentado e a marcação em três níveis de profundidade.
2. Controlo de recusa: Uma página órfã não apresenta um trilho incoerente.
3. Invariante: O trilho de navegação não revela nenhuma página não publicada.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
