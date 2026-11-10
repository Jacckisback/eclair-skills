# Plano de validação — Orçamento de peso

## Modelo de dados
Orçamento por tipo de recurso, medição, desvio.

## Implementação esperada
Fixar orçamentos por página-tipo, medir com a ferramenta do núcleo, recusar qualquer adição que os ultrapasse sem justificação.

## Testes a prever
1. Nominal: Lançar a medição dos orçamentos no site e no pacote produzido.
2. Controlo de recusa: Um pacote que ultrapassa o orçamento não é entregue tal como está.
3. Invariante: Nenhuma dependência de terceiros carregada para uma função decorativa.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
