# Plano de validação — Feeds RSS

## Modelo de dados
Feed, elementos, data, conteúdo completo ou excerto.

## Implementação esperada
Verificar o feed produzido pelo núcleo, declará-lo nas páginas, propô-lo aos subscritores e aos agregadores.

## Testes a prever
1. Nominal: Validar o feed com um leitor e um validador.
2. Controlo de recusa: Um conteúdo despublicado desaparece do feed na regeneração.
3. Invariante: O feed só contém conteúdos publicados.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
