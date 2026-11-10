# Plano de validação — Arquitetura Commerce Pro

## Modelo de dados
Catálogo, carrinho, preços fixados por linha, encomenda, pagamento, reembolso, stock, fatura e registo de estados.

## Implementação esperada
Desenhar uma máquina de estados encomenda/payment, separar a leitura pública das escritas privadas, escolher um armazenamento transacional, formalizar o conector PSP; identificar os pontos não fornecidos pelo Éclair v2.

## Testes a prever
1. Nominal: Simular compra, confirmação por webhook, nova tentativa, reembolso, stock e cancelamento.
2. Controlo de recusa: A mesma notificação de pagamento entregue duas vezes => uma única transição de encomenda.
3. Invariante: Nenhum pagamento é declarado bem-sucedido apenas com base no redirecionamento do navegador; o servidor valida um evento PSP autenticado.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
