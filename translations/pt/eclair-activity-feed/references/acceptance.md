# Plano de validação — Feed de atividade

## Modelo de dados
Evento, autor, visibilidade, data.

## Implementação esperada
Definir que eventos são publicados, para quem, e como um membro os oculta ou elimina.

## Testes a prever
1. Nominal: Simular publicações com visibilidades diferentes.
2. Controlo de recusa: Um conteúdo eliminado desaparece também do feed.
3. Invariante: Nenhuma atividade privada é revelada num feed público.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
