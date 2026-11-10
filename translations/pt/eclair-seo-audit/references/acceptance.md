# Plano de validação — Auditoria SEO técnica

## Modelo de dados
URLs, canonicals, sitemap, redirecionamentos, títulos, estados HTTP, dados estruturados.

## Implementação esperada
Rastrear as páginas autorizadas, registar as divergências, dar prioridade às causas estruturais, verificar a cobertura e o plano de correção.

## Testes a prever
1. Nominal: Testar barra final, acentos, paginações, 404, sitemap e robots.
2. Controlo de recusa: Nenhum URL crítico fica órfão ou redirecionado em cadeia após a atualização.
3. Invariante: Não prometer posições nos resultados; não modificar os URLs existentes sem um plano dos redirects.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
