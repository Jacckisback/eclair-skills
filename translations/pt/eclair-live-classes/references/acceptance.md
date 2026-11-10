# Plano de validação — Aulas em direto

## Modelo de dados
Sessão, data, fuso horário, ligação de acesso, inscritos.

## Implementação esperada
Publicar o calendário das sessões em GET, enviar a ligação de acesso pelo serviço de videoconferência ou por e-mail, não numa página pública.

## Testes a prever
1. Nominal: Verificar a apresentação das datas em dois fusos horários.
2. Controlo de recusa: Uma sessão passada deixa de ser proposta para inscrição.
3. Invariante: A ligação de uma sessão paga ou privada nunca é publicada.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
