# Plano de validação — Ferramentas de linha de comandos

## Modelo de dados
Comando, entrada, saída, código de retorno.

## Implementação esperada
Num checkout do núcleo, lançar validador, suite de testes e medição dos orçamentos; integrar estes comandos na CI do projeto.

## Testes a prever
1. Nominal: Validar um pacote e ler o relatório JSON.
2. Controlo de recusa: Um pacote inválido faz falhar o comando e a CI.
3. Invariante: Nenhum comando é lançado em produção sem cópia de segurança.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
