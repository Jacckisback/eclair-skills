# Plano de validação — Conversação em direto

## Modelo de dados
Canal, horários, ligação de conversa.

## Implementação esperada
Preferir uma ligação para um serviço de mensagens (WhatsApp, e-mail, telefone) com horários; um widget de terceiros depende da política de conteúdo nativa.

## Testes a prever
1. Nominal: Abrir o canal a partir de dispositivo móvel e de computador.
2. Controlo de recusa: Fora do horário, o site anuncia-o em vez de prometer uma resposta imediata.
3. Invariante: Nenhum widget carrega um rastreador antes de uma ação do visitante.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
