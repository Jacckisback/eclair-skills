# Plano de validação — Cartões-presente

## Modelo de dados
Cartão, código, saldo, validade.

## Implementação esperada
Gerar códigos imprevisíveis, acompanhar o saldo do lado do servidor, tratar a expiração segundo a lei aplicável.

## Testes a prever
1. Nominal: Simular compra, utilização parcial e saldo restante.
2. Controlo de recusa: Um código esgotado ou expirado é recusado.
3. Invariante: Um código nunca é adivinhável nem reutilizável para além do seu saldo.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
