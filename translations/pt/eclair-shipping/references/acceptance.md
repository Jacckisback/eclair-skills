# Plano de validação — Entrega e transporte

## Modelo de dados
Morada validada, zona, transportadora, volume, peso, serviço, custos, tracking.

## Implementação esperada
Modelar zonas e incompatibilidades; calcular a estimativa de custos do lado do servidor; prever split shipments e entrega parcial; anonimizar os dados de expedição nos registos.

## Testes a prever
1. Nominal: Testar zona não servida, peso-limite, dois volumes e estado perdido.
2. Controlo de recusa: Um número de seguimento de um cliente não deve ser visível a partir de outra conta.
3. Invariante: A morada e o seguimento são privados; nenhum dado pessoal em cache pública, logs detalhados ou URLs.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
