# Plano de validação — Paginação e listas

## Modelo de dados
Lista, página atual, tamanho de página, ligações anterior e seguinte.

## Implementação esperada
Fixar um tamanho de página razoável, endereços estáveis por página e ligações acessíveis.

## Testes a prever
1. Nominal: Percorrer a primeira página, uma página intermédia e a última.
2. Controlo de recusa: Um número de página fora dos limites responde com um erro limpo, não com uma lista vazia indexável.
3. Invariante: Os parâmetros de página são limitados e validados.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
