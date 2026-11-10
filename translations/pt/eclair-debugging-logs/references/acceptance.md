# Plano de validação — Diagnóstico e registos

## Modelo de dados
Sintoma, registo do servidor, registo do site, hipótese, correção.

## Implementação esperada
Reproduzir, ler os registos do servidor e do site, isolar a funcionalidade em causa desativando-a, corrigir e depois verificar.

## Testes a prever
1. Nominal: Provocar um erro numa extensão de teste e localizá-lo.
2. Controlo de recusa: Nenhum rasto técnico aparece numa página pública.
3. Invariante: A apresentação dos erros nunca é ativada no site público.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
