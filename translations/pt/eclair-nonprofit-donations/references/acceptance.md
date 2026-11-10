# Plano de validação — Donativos e associações

## Modelo de dados
Causa, projeto, montante, ligação de donativo, recibo.

## Implementação esperada
Apresentar a missão e a utilização dos fundos, ligar os botões de donativo a ligações do prestador, remeter a gestão dos recibos para o prestador ou para a associação.

## Testes a prever
1. Nominal: Fazer um donativo em modo de teste e seguir o percurso completo.
2. Controlo de recusa: Um montante modificado na página não altera o montante cobrado.
3. Invariante: Nenhuma promessa de benefício fiscal sem confirmação da associação.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
