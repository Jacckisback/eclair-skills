# Plano de validação — Ligações de afiliado

## Modelo de dados
Ligação, programa, menção, conteúdo de suporte.

## Implementação esperada
Ativar a extensão de afiliação fornecida, declarar os programas, deixar o núcleo adicionar a menção e o atributo de patrocínio.

## Testes a prever
1. Nominal: Publicar um comparativo e verificar a menção e os atributos das ligações.
2. Controlo de recusa: Uma ligação de afiliado nunca é apresentada como uma opinião independente.
3. Invariante: Nenhuma ligação de afiliado sem menção publicitária visível.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
