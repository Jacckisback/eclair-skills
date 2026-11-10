# Plano de validação — Migração WordPress

## Modelo de dados
Exportação WordPress, IDs antigos, slugs, multimédia, categorias, autores, redirecionamentos e pedidos ?p=.

## Implementação esperada
Utilizar a extensão nativa WordPress; inventariar os URLs históricos, simular a importação, comparar slug/canonical, conservar as ligações exatas e os ficheiros multimédia, fornecer um plano de rollback.

## Testes a prever
1. Nominal: Testar URL com barra final, query alias, acentos, imagens e páginas eliminadas.
2. Controlo de recusa: Para cada URL antigo indexado, obter um 200 exato ou um redirecionamento 301 direcionado.
3. Invariante: Evitar erros 404 e eliminações de URLs; nunca fazer a mudança de DNS sem testes e cópias de segurança.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
