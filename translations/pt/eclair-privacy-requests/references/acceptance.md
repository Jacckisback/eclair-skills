# Plano de validação — Pedidos relativos aos dados

## Modelo de dados
Pedido, pessoa, dados em causa, prazo, resposta.

## Implementação esperada
Mapear onde estão os dados (mensagens, contas, registos, cópias de segurança), escrever o procedimento de acesso e de apagamento, manter um registo.

## Testes a prever
1. Nominal: Percorrer um pedido de acesso e depois de apagamento num conjunto de teste.
2. Controlo de recusa: Um pedido sem verificação de identidade não conduz a nenhuma divulgação.
3. Invariante: A identidade do requerente é verificada antes de qualquer comunicação de dados.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
