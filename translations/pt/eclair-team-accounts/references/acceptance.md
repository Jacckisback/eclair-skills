# Plano de validação — Contas da equipa

## Modelo de dados
Conta, direitos, autenticação de dois fatores, último início de sessão.

## Implementação esperada
Listar quem faz o quê, atribuir os direitos nativos mínimos, impor a autenticação de dois fatores, retirar as contas inúteis.

## Testes a prever
1. Nominal: Criar uma conta de redator e verificar o que pode e não pode fazer.
2. Controlo de recusa: Uma conta sem o direito Definições não pode ativar uma funcionalidade nem mudar de tema.
3. Invariante: Nenhuma conta partilhada; nenhum direito Segurança concedido por comodidade.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
