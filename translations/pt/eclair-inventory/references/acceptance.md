# Plano de validação — Stocks e reservas

## Modelo de dados
SKU, armazém, stock físico, reservado, disponível, movimentos imutáveis.

## Implementação esperada
Conceber os movimentos de entrada/saída; bloquear a reserva; gerir a expiração e a compensação; rastrear todas as correções manuais.

## Testes a prever
1. Nominal: Testar compras simultâneas do último exemplar e a libertação após expiração.
2. Controlo de recusa: Dois compradores não podem reservar o mesmo último stock.
3. Invariante: A leitura de disponibilidade armazenável em cache é informativa; qualquer venda volta a ler o stock numa transação.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
