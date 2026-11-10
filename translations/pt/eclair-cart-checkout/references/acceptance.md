# Plano de validação — Carrinho e processo de encomenda

## Modelo de dados
Carrinho temporário, sessão de membro ou de convidado, linhas, promoções, custos, impostos, estado da encomenda.

## Implementação esperada
Separar a apresentação da mudança de estado; revalidar cada linha no servidor; calcular os montantes em unidades monetárias inteiras; reservar o stock de forma transacional no momento certo.

## Testes a prever
1. Nominal: Testar a modificação simultânea do carrinho, a expiração e a alteração de preço.
2. Controlo de recusa: Uma submissão dupla ou concorrente não cria duas encomendas pagáveis para a mesma chave.
3. Invariante: Nenhuma operação de escrita pública antes de rota POST qualificada, CSRF, quotas e permissões verificados.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
