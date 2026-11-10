# Plano de validação — Moderação e denúncias

## Modelo de dados
Denúncia, motivo, elemento visado, decisão, moderador, auditoria.

## Implementação esperada
Prever fila de tratamento, denúncias abusivas, limiares/quotas, rollback e motivos; registar decisões e restringir poderes por papel.

## Testes a prever
1. Nominal: Testar moderador sem direito global, utilizador suspenso e recurso.
2. Controlo de recusa: Um moderador de uma categoria não consegue ver as denúncias privadas de outra.
3. Invariante: Nenhuma eliminação definitiva automática por denúncia sem controlo e provas.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
