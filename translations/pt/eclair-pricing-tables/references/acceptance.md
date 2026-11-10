# Plano de validação — Tabelas de preços

## Modelo de dados
Oferta, preço, período, características, botão.

## Implementação esperada
Compor as ofertas em cartões comparáveis, apresentar os preços com IVA ou sem IVA sem ambiguidade e ligar cada botão à ação correta.

## Testes a prever
1. Nominal: Comparar três ofertas num dispositivo móvel e verificar cada ligação.
2. Controlo de recusa: Uma oferta sem preço validado não é apresentada.
3. Invariante: Nenhum preço, desconto ou menção legal inventados.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
