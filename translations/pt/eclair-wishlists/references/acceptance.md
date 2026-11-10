# Plano de validação — Listas de desejos

## Modelo de dados
Lista, produto, proprietário.

## Implementação esperada
Começar por um armazenamento no navegador sem conta; conceber a versão com conta para mais tarde.

## Testes a prever
1. Nominal: Adicionar, remover e reencontrar favoritos.
2. Controlo de recusa: Um produto eliminado desaparece corretamente das listas.
3. Invariante: Nenhuma lista é partilhada ou visível por terceiros sem ação do proprietário.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
