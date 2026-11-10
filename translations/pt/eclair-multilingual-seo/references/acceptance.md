# Plano de validação — SEO multilingue

## Modelo de dados
Língua, URL de tradução, hreflang recíproco, título e sitemap.

## Implementação esperada
Inventariar as línguas publicadas, definir o mapping das traduções, testar canonical por língua, hreflang/x-default e ausência de redirecionamento intrusivo.

## Testes a prever
1. Nominal: Testar pares FR/ES/EN, páginas em falta e mudança de língua.
2. Controlo de recusa: Cada ligação hreflang aponta para um URL 200 indexável e recíproco.
3. Invariante: Não utilizar uma tradução automática não verificada como página definitiva.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
