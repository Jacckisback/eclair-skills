# Plano de validação — Sondagens e inquéritos

## Modelo de dados
Pergunta, opções, resposta, participante anónimo, resultados agregados.

## Implementação esperada
Definir o anonimato, a limitação dos votos múltiplos, a apresentação dos resultados agregados e a duração da sondagem.

## Testes a prever
1. Nominal: Votar, consultar os resultados e encerrar a sondagem.
2. Controlo de recusa: Um segundo voto do mesmo participante é ignorado.
3. Invariante: Nenhuma resposta individual é publicada; apenas resultados agregados.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
