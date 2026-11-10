# Plano de validação — Faixas de anúncio

## Modelo de dados
Mensagem, ligação, datas de início e de fim.

## Implementação esperada
Renderizar a faixa do lado do servidor com datas de validade, sem deslocamento da disposição, retirada automaticamente no termo do prazo.

## Testes a prever
1. Nominal: Apresentar, fechar e deixar expirar uma faixa.
2. Controlo de recusa: Após a data de fim, a faixa já não aparece em nenhuma página.
3. Invariante: Nenhum anúncio expirado continua a ser servido pela cache.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
