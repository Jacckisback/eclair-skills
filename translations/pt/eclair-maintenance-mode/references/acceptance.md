# Plano de validação — Modo de manutenção

## Modelo de dados
Estado de manutenção, mensagem, duração prevista, acesso da equipa.

## Implementação esperada
Servir uma página estática com o estado HTTP temporário correto ao nível do servidor, manter o acesso à administração, prever o regresso online.

## Testes a prever
1. Nominal: Ativar, verificar estado 503 e cabeçalho de nova tentativa, desativar.
2. Controlo de recusa: Os robôs nunca recebem a página de manutenção com um estado 200.
3. Invariante: A página de manutenção não revela nem a versão nem o caminho do servidor.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
