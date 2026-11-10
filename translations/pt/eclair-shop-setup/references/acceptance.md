# Plano de validação — Abertura da loja leve

## Modelo de dados
Produto, preço, categoria, menções legais, condições de venda.

## Implementação esperada
Publicar as menções legais e as condições de venda, abrir a loja, criar as primeiras fichas, verificar o catálogo e os dados estruturados.

## Testes a prever
1. Nominal: Abrir a loja numa cópia e percorrer o catálogo e uma ficha.
2. Controlo de recusa: A loja não abre sem páginas legais publicadas.
3. Invariante: Nenhum preço, prazo ou condição de venda inventados pelo agente.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
