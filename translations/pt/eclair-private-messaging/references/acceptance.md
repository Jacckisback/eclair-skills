# Plano de validação — Mensagens privadas

## Modelo de dados
Conversa, participantes, mensagem, denúncia.

## Implementação esperada
Definir bloqueio, denúncia, limites de envio e conservação; nenhuma conversa numa página em cache.

## Testes a prever
1. Nominal: Simular troca de mensagens, bloqueio e denúncia.
2. Controlo de recusa: Um membro bloqueado já não consegue escrever a quem o bloqueou.
3. Invariante: Uma mensagem só é legível pelos seus participantes.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
