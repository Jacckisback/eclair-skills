# Plano de validação — Produtos digitais

## Modelo de dados
Produto digital, compra, ligação de entrega temporária.

## Implementação esperada
Fazer entregar o ficheiro pelo prestador ou por ligação assinada de duração limitada; nunca colocar o ficheiro num endereço público.

## Testes a prever
1. Nominal: Simular compra, entrega e expiração da ligação.
2. Controlo de recusa: Uma ligação expirada ou partilhada deixa de dar acesso ao ficheiro.
3. Invariante: Nenhum ficheiro pago é acessível sem compra verificada.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
