# Plano de validação — Search Console

## Modelo de dados
Propriedade, método de verificação, sitemap declarado, relatórios.

## Implementação esperada
Verificar o domínio por registo DNS, declarar o sitemap nativo, ler cobertura e consultas todos os meses.

## Testes a prever
1. Nominal: Verificar a propriedade e a tomada em conta do sitemap.
2. Controlo de recusa: Um erro de cobertura é explicado, não ocultado.
3. Invariante: Nenhum acesso de proprietário concedido a terceiros sem acordo do cliente.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
