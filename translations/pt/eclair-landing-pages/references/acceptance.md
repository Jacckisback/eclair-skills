# Plano de validação — Páginas de destino

## Modelo de dados
Promessa, provas, oferta, chamada à ação.

## Implementação esperada
Escrever uma página para uma única intenção, compô-la em blocos nativos, ligar a ação a um formulário ou a uma ligação de pagamento.

## Testes a prever
1. Nominal: Percorrer a página num dispositivo móvel até à ação.
2. Controlo de recusa: Uma prova não fornecida pelo cliente não aparece.
3. Invariante: Nenhum testemunho, número ou garantia inventados.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
