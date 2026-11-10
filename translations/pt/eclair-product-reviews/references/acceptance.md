# Plano de validação — Avaliações de produtos

## Modelo de dados
Avaliação, classificação, autor, compra verificada, estado.

## Implementação esperada
Definir prova de compra, moderação, direito de resposta e apresentação agregada; propor, até lá, testemunhos recolhidos manualmente.

## Testes a prever
1. Nominal: Simular envio, moderação e publicação de uma avaliação.
2. Controlo de recusa: Uma avaliação sem compra verificada não é marcada como verificada.
3. Invariante: Nenhuma avaliação publicada sem moderação; nenhuma classificação agregada sem avaliações reais.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
