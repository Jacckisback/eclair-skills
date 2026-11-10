# Plano de validação — Mensagens recebidas

## Modelo de dados
Mensagem, estado, resposta, prazo de conservação.

## Implementação esperada
Definir quem lê e responde, em que prazo, durante quanto tempo as mensagens são conservadas e como são eliminadas.

## Testes a prever
1. Nominal: Tratar uma mensagem desde a receção até ao arquivo.
2. Controlo de recusa: Uma conta sem a permissão Mensagens não acede a nenhuma mensagem.
3. Invariante: Prazo de conservação limitado e permissão de acesso restrita.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
