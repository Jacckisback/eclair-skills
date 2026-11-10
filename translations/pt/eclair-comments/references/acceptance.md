# Plano de validação — Comentários

## Modelo de dados
Comentário, autor, estado de moderação, artigo, data.

## Implementação esperada
Definir fila de moderação, regras antisspam, menções legais e apresentação em cache; propor, entretanto, um serviço externo ou um pedido de contacto.

## Testes a prever
1. Nominal: Simular o envio, a moderação, a publicação e a eliminação de um comentário.
2. Controlo de recusa: Um comentário pendente ou recusado nunca aparece numa página em cache.
3. Invariante: Nenhum comentário é apresentado sem moderação; nenhum endereço de e-mail é tornado público.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
