# Plano de validação — Glossário

## Modelo de dados
Termo, definição, termos relacionados.

## Implementação esperada
Redigir uma definição clara por termo, ordenar por ordem alfabética, ligar os termos aos conteúdos que os utilizam.

## Testes a prever
1. Nominal: Navegar por letra e seguir as ligações entre termos.
2. Controlo de recusa: Um termo sem definição validada não é publicado.
3. Invariante: Nenhuma definição copiada de uma fonte protegida.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
