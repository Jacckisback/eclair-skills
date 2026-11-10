# Plano de validação — Simuladores e calculadoras

## Modelo de dados
Parâmetros, fórmula, resultado.

## Implementação esperada
Calcular no navegador com uma fórmula validada pelo cliente, apresentar os pressupostos e os limites, propor em seguida o contacto.

## Testes a prever
1. Nominal: Comparar os resultados com um conjunto de casos calculados à mão.
2. Controlo de recusa: Um valor absurdo ou negativo apresenta uma mensagem, não um resultado errado.
3. Invariante: O resultado é indicativo e anunciado como tal; nenhum dado introduzido é enviado para o servidor.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
