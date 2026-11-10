# Plano de validação — Dados estruturados

## Modelo de dados
WebPage, Article, Product, FAQ pertinente, Organization, BreadcrumbList.

## Implementação esperada
Inspecionar o JSON-LD nativo antes de adicionar um tipo; evitar duplicação; alinhar cada campo com os dados visíveis e as diretrizes dos motores de pesquisa.

## Testes a prever
1. Nominal: Testar JSON válido, canonical, identificadores e conteúdo apresentado.
2. Controlo de recusa: Nenhum preço/avaliação/product inventado ou ausente da página figura no JSON-LD.
3. Invariante: O Éclair v2 ainda não expõe todas as contribuições JSON-LD às extensões; propor uma RFC em vez de uma injeção opaca.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
