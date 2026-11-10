# Plano de validação — Medição de audiência respeitadora da privacidade

## Modelo de dados
Página vista, origem, período, agregados.

## Implementação esperada
Preferir os registos do servidor ou uma ferramenta sem cookies em alojamento próprio; um script de terceiros depende da política de conteúdo nativa.

## Testes a prever
1. Nominal: Comparar as páginas vistas medidas com um percurso de teste.
2. Controlo de recusa: Nenhum cookie é depositado pela medição.
3. Invariante: Nenhum endereço IP completo nem identificador de visitante é conservado.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
