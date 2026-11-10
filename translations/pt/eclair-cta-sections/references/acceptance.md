# Plano de validação — Chamadas à ação

## Modelo de dados
Título, texto, botão, destino.

## Implementação esperada
Definir uma ação principal por página, repeti-la nos sítios certos, verificar o contraste e o texto explícito do botão.

## Testes a prever
1. Nominal: Seguir cada botão até ao seu destino num dispositivo móvel.
2. Controlo de recusa: Um botão sem destino válido não é publicado.
3. Invariante: Nenhuma ligação enganadora nem redirecionamento aberto.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
