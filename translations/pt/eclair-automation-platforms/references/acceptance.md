# Plano de validação — Plataformas de automatização

## Modelo de dados
Cenário, acionador, dados transmitidos.

## Implementação esperada
Expor em leitura o que a plataforma pode consultar (feeds, JSON público); conceber a receção de eventos para mais tarde.

## Testes a prever
1. Nominal: Fazer a plataforma ler um feed público e desencadear um cenário.
2. Controlo de recusa: Uma chamada de entrada não autenticada não modifica nada no site.
3. Invariante: Nenhum dado pessoal é exposto num ponto de acesso público para facilitar uma automatização.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
