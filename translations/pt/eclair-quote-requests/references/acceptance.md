# Plano de validação — Pedidos de orçamento

## Modelo de dados
Pedido, serviço, orçamento disponível, prazo, contactos.

## Implementação esperada
Começar com o formulário de contacto nativo e perguntas orientadas na página; conceber o formulário estruturado para mais tarde.

## Testes a prever
1. Nominal: Enviar um pedido-tipo e verificar a sua receção completa.
2. Controlo de recusa: Um pedido sem contactos válidos é recusado com uma mensagem clara.
3. Invariante: Só são pedidos os dados úteis para o orçamento.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
