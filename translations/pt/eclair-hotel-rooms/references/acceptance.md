# Plano de validação — Alojamentos e quartos

## Modelo de dados
Quarto, capacidade, equipamentos, tarifas indicativas, ligação de reserva.

## Implementação esperada
Apresentar cada alojamento numa ficha, remeter para o motor de reservas existente ou para o pedido por formulário.

## Testes a prever
1. Nominal: Percorrer fichas e ligação de reserva em dispositivo móvel.
2. Controlo de recusa: Um quarto retirado deixa de ser proposto.
3. Invariante: Nenhuma disponibilidade nem tarifa apresentadas como garantidas se não vierem do sistema de reservas.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
