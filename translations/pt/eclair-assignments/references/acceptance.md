# Plano de validação — Trabalhos e correções

## Modelo de dados
Trabalho, entrega, nota, comentário, formando.

## Implementação esperada
Definir entrega, prazos, correção e devolução; isolar cada trabalho entregue ao seu autor e ao corretor.

## Testes a prever
1. Nominal: Simular entrega, correção e consulta da nota.
2. Controlo de recusa: Um formando não consegue aceder ao trabalho entregue de outro.
3. Invariante: Um trabalho entregue só é legível pelo seu autor e pelos corretores designados.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
