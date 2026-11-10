# Plano de validação — Categorias

## Modelo de dados
Categoria, endereço, descrição, conteúdos associados.

## Implementação esperada
Definir poucas categorias estáveis, redigir a respetiva descrição, associar cada conteúdo a uma categoria principal.

## Testes a prever
1. Nominal: Criar as categorias, associar os conteúdos e verificar as páginas de categoria e a respetiva paginação.
2. Controlo de recusa: Uma categoria sem conteúdo publicado não é proposta na navegação.
3. Invariante: Não criar categorias vazias ou duplicadas que diluam o site.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
