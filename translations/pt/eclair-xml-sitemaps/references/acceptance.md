# Plano de validação — Sitemap XML

## Modelo de dados
Entradas de sitemap, datas, imagens, línguas.

## Implementação esperada
Verificar o sitemap produzido pelo núcleo, declará-lo nas ferramentas dos motores de pesquisa, vigiar os erros de cobertura.

## Testes a prever
1. Nominal: Validar o sitemap e comparar com o número de páginas publicadas.
2. Controlo de recusa: Uma página em rascunho ou redirecionada não figura nele.
3. Invariante: O sitemap só lista páginas publicadas e indexáveis.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
