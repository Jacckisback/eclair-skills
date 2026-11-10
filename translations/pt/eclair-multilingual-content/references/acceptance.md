# Plano de validação — Conteúdos multilingues

## Modelo de dados
Conteúdo, língua, versão ligada, endereço por língua.

## Implementação esperada
Verificar nas capacidades as línguas suportadas pelo site, organizar uma estrutura em árvore por língua, ligar as versões e verificar hreflang.

## Testes a prever
1. Nominal: Criar uma página em duas línguas e verificar as ligações cruzadas e hreflang.
2. Controlo de recusa: Uma língua sem tradução não remete para uma página vazia.
3. Invariante: Nenhuma tradução automática é publicada sem revisão humana.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
