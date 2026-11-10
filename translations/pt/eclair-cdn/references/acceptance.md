# Plano de validação — Rede de distribuição (CDN)

## Modelo de dados
Zona DNS, regras de cache, purga.

## Implementação esperada
Configurar DNS e HTTPS de ponta a ponta, excluir a administração da cache do CDN, definir a purga na publicação.

## Testes a prever
1. Nominal: Verificar cabeçalhos de cache das páginas públicas e da administração.
2. Controlo de recusa: Após modificação, a versão antiga deixa de ser servida depois da purga.
3. Invariante: A administração e qualquer resposta privada nunca são colocadas em cache pelo CDN.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
