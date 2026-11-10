# Plano de validação — Autenticação de dois fatores

## Modelo de dados
Conta, segredo TOTP, códigos de recuperação.

## Implementação esperada
Fazer ativar a autenticação de dois fatores por cada pessoa, guardar os códigos de recuperação, prever a perda do dispositivo.

## Testes a prever
1. Nominal: Ativar, terminar sessão, voltar a iniciar sessão com o segundo fator.
2. Controlo de recusa: Uma palavra-passe correta sem segundo fator não dá acesso.
3. Invariante: Os segredos e os códigos de recuperação nunca são copiados para um chat, um e-mail ou um repositório.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
