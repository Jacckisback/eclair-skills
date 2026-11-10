# Plano de validação — Atualizações e reversão

## Modelo de dados
Versão instalada, versão anunciada, assinatura, ponto de retorno.

## Implementação esperada
Fazer cópia de segurança, ler as notas de versão, lançar a atualização com um clique, verificar o site, saber regressar à versão anterior.

## Testes a prever
1. Nominal: Atualizar uma cópia do site e depois reverter.
2. Controlo de recusa: Um anúncio de atualização não assinado pelo mantenedor é recusado.
3. Invariante: Nunca instalar um arquivo cuja assinatura não seja verificada pelo núcleo.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
