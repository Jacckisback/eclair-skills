# Plano de validação — Campanhas de e-mail

## Modelo de dados
Lista, segmento, campanha, envio, cancelamento da subscrição.

## Implementação esperada
Confiar o envio a um serviço especializado, preparar os conteúdos a partir do site, definir segmentos, frequência e cancelamento da subscrição.

## Testes a prever
1. Nominal: Enviar uma campanha de teste para uma lista interna.
2. Controlo de recusa: Um endereço que cancelou a subscrição não recebe mais nada.
3. Invariante: Cada e-mail contém uma ligação funcional de cancelamento da subscrição; nenhuma lista comprada.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
