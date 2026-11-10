# Plano de validação — Cabeçalhos de segurança

## Modelo de dados
Cabeçalhos HTTP, Content-Security-Policy, HTTPS.

## Implementação esperada
Levantar os cabeçalhos servidos, verificar HTTPS em todo o lado, testar as regras do servidor web fornecidas com o núcleo.

## Testes a prever
1. Nominal: Analisar os cabeçalhos de uma página pública e da administração.
2. Controlo de recusa: Um ficheiro sensível ou de dados nunca é servido pelo servidor web.
3. Invariante: Nenhum cabeçalho de proteção é retirado nem flexibilizado.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
